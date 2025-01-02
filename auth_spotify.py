import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="*****",
    client_secret="*****",
    redirect_uri="http://localhost:8888/callback",
    scope=scope
))

# Kullanıcının beğendiği şarkıları al
results = sp.current_user_saved_tracks()
print("Spotify bağlantısı başarılı!")
print(f"Beğenilen şarkı sayısı: {results['total']}") 
