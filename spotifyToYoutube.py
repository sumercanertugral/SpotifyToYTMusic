#coding: utf-8

# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from ytmusicapi import YTMusic
import json

class SpotifyToYoutube:
    def __init__(self):
        self.ytmusic = YTMusic('ytmusic_headers.json')

    def add_to_playlist(self, target_playlist, track_name):
        try:
            print(f"Adding track: {track_name}")
            search_results = self.ytmusic.search(track_name, filter="songs")
            if len(search_results) > 0:
                try:
                    self.ytmusic.add_playlist_items(target_playlist, [search_results[0]['videoId']])
                except Exception as e:
                    print(f"An exception occurred: {str(e)}")
                    print(e)
            else:
                print(f"No results found for {track_name}")
        except Exception as e:
            print(f"An exception occurred: {str(e)}")
            print(e)

    def get_tracks(self, playlist_url, client_id, client_secret):
        spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="http://localhost:8888/callback",
            scope="user-library-read"
        ))
        
        if playlist_url == "me":
            # Beğenilen şarkıları al
            results = spotify.current_user_saved_tracks()
            tracks = []
            items = results['items']
            
            # Tüm şarkıları al (sayfalama)
            while results['next']:
                results = spotify.next(results)
                items.extend(results['items'])
            
            for item in items:
                track = item['track']
                tracks.append(track['name'] + " - " + track['artists'][0]['name'])
        else:
            # Normal playlist şarkılarını al
            results = spotify.user_playlist_tracks(user="", playlist_id=playlist_url)
            tracks = []
            for idx, item in enumerate(results['items']):
                track = item['track']
                tracks.append(track['name'] + " - " + track['artists'][0]['name'])
        return tracks
