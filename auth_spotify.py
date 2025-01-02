import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="7971cf9510574e838ae2698488b0be25",
    client_secret="703e75a254a34f67ab79bb6422d23f47",
    redirect_uri="http://localhost:8888/callback",
    scope=scope
))

# Kullanıcının beğendiği şarkıları al
results = sp.current_user_saved_tracks()
print("Spotify bağlantısı başarılı!")
print(f"Beğenilen şarkı sayısı: {results['total']}") 