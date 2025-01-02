#coding: utf-8

# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from ytmusicapi import YTMusic
import json
import time
import re
import logging

class SpotifyToYoutube:
    def __init__(self, failed_songs_logger=None):
        self.failed_songs_logger = failed_songs_logger
        self.load_config()
        self.setup_spotify()
        self.setup_youtube()
        
    def setup_spotify(self):
        scope = "user-library-read playlist-read-private"
        self.spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=self.config['spotify']['client_id'],
            client_secret=self.config['spotify']['client_secret'],
            redirect_uri="http://localhost:8888/callback",
            scope=scope
        ))

    def setup_youtube(self):
        self.ytmusic = YTMusic('ytmusic_headers.json')

    def load_config(self):
        with open('config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)

    def get_spotify_tracks(self, playlist_id):
        if playlist_id == "liked":
            results = self.spotify.current_user_saved_tracks()
            tracks = results['items']
            while results['next']:
                results = self.spotify.next(results)
                tracks.extend(results['items'])
            return [(track['track']['name'], track['track']['artists'][0]['name']) for track in tracks]
        else:
            results = self.spotify.playlist_tracks(playlist_id)
            tracks = results['items']
            while results['next']:
                results = self.spotify.next(results)
                tracks.extend(results['items'])
            return [(track['track']['name'], track['track']['artists'][0]['name']) for track in tracks]

    def create_youtube_playlist(self, name):
        try:
            playlist_id = self.ytmusic.create_playlist(name, "Spotify'dan aktarılan çalma listesi")
            return playlist_id
        except Exception as e:
            if self.failed_songs_logger:
                self.failed_songs_logger.error(f"Playlist oluşturma hatası: {str(e)}")
            raise

    def search_and_add_to_playlist(self, track_name, artist_name, playlist_id):
        try:
            print(f"\n[{self.current_track}/{self.total_tracks}] İşleniyor: {track_name} - {artist_name}")
            search_query = f"{track_name} {artist_name}"
            search_results = self.ytmusic.search(search_query, filter="songs")
            
            if not search_results:
                if self.failed_songs_logger:
                    self.failed_songs_logger.error(f"Şarkı bulunamadı: {track_name} - {artist_name}")
                return False
            
            video_id = search_results[0]['videoId']
            self.ytmusic.add_playlist_items(playlist_id, [video_id])
            print(f"✓ Bulundu: {track_name}")
            return True
            
        except Exception as e:
            if self.failed_songs_logger:
                self.failed_songs_logger.error(f"Şarkı eklenirken hata: {track_name} - {artist_name} - Hata: {str(e)}")
            return False

    def migrate_playlists(self):
        for spotify_key, spotify_playlist_id in self.config['spotify']['playlists'].items():
            youtube_playlist_name = self.config['google']['playlists'][spotify_key]
            
            # Spotify'dan şarkıları al
            tracks = self.get_spotify_tracks(spotify_playlist_id)
            self.total_tracks = len(tracks)
            print(f"\nToplam {self.total_tracks} şarkı bulundu.")
            
            # YouTube Music'te playlist oluştur
            youtube_playlist_id = self.create_youtube_playlist(youtube_playlist_name)
            
            # Her şarkıyı ekle
            successful_tracks = 0
            self.current_track = 0
            
            for track_name, artist_name in tracks:
                self.current_track += 1
                if self.search_and_add_to_playlist(track_name, artist_name, youtube_playlist_id):
                    successful_tracks += 1
                    
                # Her 50 şarkıda bir bilgi ver
                if successful_tracks > 0 and successful_tracks % 50 == 0:
                    print(f"\n✓ {successful_tracks} şarkı playlist'e eklendi\n")
