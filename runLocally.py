#coding: utf-8
import json
from spotifyToYoutube import SpotifyToYoutube
import argparse
from spotipy.oauth2 import SpotifyOAuth
import spotipy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--spotify_client_id')
    parser.add_argument('--spotify_client_secret')
    args = parser.parse_args()

    with open('config.json') as f:
        jsonConfig = json.load(f)

    spotifyToYoutube = SpotifyToYoutube()

    for i in range(len(jsonConfig["spotify"]["playlists"])):
        playlist_url = jsonConfig["spotify"]["playlists"][i]
        target_playlist = jsonConfig["google"]["playlists"][i]
        print(f"Source: {playlist_url}")
        print(f"Target: {target_playlist}")

        print("Getting tracks...")
        tracks = spotifyToYoutube.get_tracks(playlist_url, args.spotify_client_id or jsonConfig["spotify"]["client_id"], args.spotify_client_secret or jsonConfig["spotify"]["client_secret"])

        print(f"Found {len(tracks)} tracks")
        for track in tracks:
            spotifyToYoutube.add_to_playlist(target_playlist, track)

    print("Migration finished!")

if __name__ == "__main__":
    main()
    
