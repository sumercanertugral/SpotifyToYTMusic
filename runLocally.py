#coding: utf-8
import json
from spotifyToYoutube import SpotifyToYoutube
import argparse
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import logging
import sys
import os
from datetime import datetime

# Log dosyası ayarları
def setup_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    log_filename = f'logs/transfer_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    error_filename = f'logs/failed_songs_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
    
    # Ana log için ayarlar
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Hata veren şarkılar için özel logger
    failed_songs_logger = logging.getLogger('failed_songs')
    failed_songs_logger.setLevel(logging.ERROR)
    failed_handler = logging.FileHandler(error_filename, encoding='utf-8')
    failed_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    failed_songs_logger.addHandler(failed_handler)
    
    return logging.getLogger(__name__), failed_songs_logger

def update_config_for_liked_songs():
    logger.info("Beğenilen şarkılar için config dosyası güncelleniyor...")
    config = {
        "spotify": {
            "client_id": "7971cf9510574e838ae2698488b0be25",
            "client_secret": "703e75a254a34f67ab79bb6422d23f47",
            "playlists": {
                "liked": "liked"
            }
        },
        "google": {
            "playlists": {
                "liked": "Spotify Beğenilen Şarkılar"
            }
        }
    }
    
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    logger.info("Config dosyası güncellendi.")

def update_config_for_playlist():
    logger.info("Özel playlist için bilgiler isteniyor...")
    spotify_playlist_id = input("\nSpotify playlist ID'sini girin (örn: 5LI3TG6Yfp7dbud9R5hsj9): ").strip()
    youtube_playlist_name = input("YouTube Music'te oluşturulacak playlist adını girin (örn: Favori Şarkılarım): ").strip()
    
    config = {
        "spotify": {
            "client_id": "7971cf9510574e838ae2698488b0be25",
            "client_secret": "703e75a254a34f67ab79bb6422d23f47",
            "playlists": {
                "custom_playlist": spotify_playlist_id
            }
        },
        "google": {
            "playlists": {
                "custom_playlist": youtube_playlist_name
            }
        }
    }
    
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    logger.info(f"Config dosyası güncellendi. Spotify ID: {spotify_playlist_id}, YouTube Playlist: {youtube_playlist_name}")

def show_menu():
    while True:
        print("\n" + "="*50)
        print("     Spotify -> YouTube Music Aktarım Aracı")
        print("="*50)
        print("\nLütfen yapmak istediğiniz işlemi seçin:")
        print("\n1. Beğenilen şarkıları aktar")
        print("2. Özel playlist aktar")
        print("3. Çıkış")
        
        try:
            choice = input("\nSeçiminiz (1-3): ").strip()
            
            if choice == "1":
                logger.info("Beğenilen şarkıları aktarma seçeneği seçildi.")
                print("\nBeğenilen şarkılar aktarılacak...")
                update_config_for_liked_songs()
                return True
            elif choice == "2":
                logger.info("Özel playlist aktarma seçeneği seçildi.")
                print("\nPlaylist ID'lerini girmeniz gerekiyor:")
                print("\nSpotify playlist ID'sini almak için:")
                print("1. Spotify'da playlist'e gidin")
                print("2. Share > Copy link to playlist'e tıklayın")
                print("3. Linkteki ID'yi kopyalayın (örn: spotify.com/playlist/5LI3TG6Yfp7dbud9R5hsj9)")
                
                update_config_for_playlist()
                return True
            elif choice == "3":
                logger.info("Program sonlandırılıyor...")
                print("\nProgram sonlandırılıyor...")
                return False
            else:
                print("\nGeçersiz seçim! Lütfen 1-3 arası bir sayı girin.")
                logger.warning(f"Geçersiz seçim yapıldı: {choice}")
        except Exception as e:
            logger.error(f"Menü seçiminde hata: {str(e)}")
            print("\nBir hata oluştu! Lütfen tekrar deneyin.")

def main():
    try:
        global logger, failed_songs_logger
        logger, failed_songs_logger = setup_logging()
        logger.info("Program başlatıldı.")
        
        if show_menu():
            logger.info("Aktarım işlemi başlatılıyor...")
            spotify_to_youtube = SpotifyToYoutube(failed_songs_logger)
            spotify_to_youtube.migrate_playlists()
            logger.info("Aktarım işlemi tamamlandı.")
            
    except Exception as e:
        logger.error(f"Kritik hata: {str(e)}")
        print(f"\nBir hata oluştu: {str(e)}")
    finally:
        logger.info("Program sonlandı.")

if __name__ == "__main__":
    main()
    
