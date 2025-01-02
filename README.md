# Spotify'dan YouTube Music'e Şarkı Aktarma Aracı

Bu araç, Spotify çalma listelerinizi veya beğendiğiniz şarkıları YouTube Music'e otomatik olarak aktarmanızı sağlar.

## Özellikler

- Spotify'daki beğenilen şarkıları YouTube Music'e aktarma
- Spotify çalma listelerini YouTube Music'e aktarma
- Otomatik şarkı eşleştirme ve ekleme

## Gereksinimler

- Python 3.6 veya üzeri
- pip (Python paket yöneticisi)
- Spotify hesabı
- YouTube Music hesabı

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. Örnek yapılandırma dosyalarını kopyalayın:
```bash
cp config.example.json config.json
cp ytmusic_headers.example.json ytmusic_headers.json
```

3. `config.json` dosyasını düzenleyin:
```json
{
    "spotify": {
        "client_id": "YOUR_SPOTIFY_CLIENT_ID",
        "client_secret": "YOUR_SPOTIFY_CLIENT_SECRET",
        "playlists": ["liked"]
    },
    "google": {
        "playlists": ["Spotify Beğenilen Şarkılar"]
    }
}
```

- Spotify API bilgilerini almak için:
  1. [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)'a gidin
  2. Yeni bir uygulama oluşturun
  3. Client ID ve Client Secret bilgilerini `config.json` dosyasına ekleyin

4. YouTube Music cookie bilgilerini alın:
  1. Chrome tarayıcısında YouTube Music'e giriş yapın
  2. Developer Tools'u açın (F12 veya Cmd+Option+I)
  3. Network sekmesine gidin
  4. Sayfayı yenileyin ve cookie değerlerini kopyalayın
  5. `ytmusic_headers.json` dosyasındaki ilgili alanları güncelleyin

## Kullanım

1. Spotify kimlik doğrulaması için:
```bash
python3 auth_spotify.py
```

2. Şarkıları aktarmak için:
```bash
python3 runLocally.py
```

## Notlar

- İlk çalıştırmada Spotify hesabınıza giriş yapmanız istenecektir
- Program, şarkıları YouTube Music'te arayıp en uygun eşleşmeyi bulmaya çalışacaktır
- Aktarım sırasında bazı şarkılar bulunamayabilir veya farklı versiyonları eklenebilir

## Dosya Yapısı

- `spotifyToYoutube.py`: Ana program dosyası
- `config.json`: Yapılandırma dosyası
- `runLocally.py`: Yerel çalıştırma betiği
- `auth_spotify.py`: Spotify kimlik doğrulama dosyası
- `ytmusic_headers.json`: YouTube Music çerez bilgileri
- `.cache`: Spotify oturum önbelleği
- `requirements.txt`: Python bağımlılıkları

## Sorun Giderme

1. Spotify API hatası alırsanız:
   - Client ID ve Client Secret bilgilerinin doğru olduğundan emin olun
   - Spotify Developer Dashboard'da uygulamanızın aktif olduğunu kontrol edin

2. YouTube Music hatası alırsanız:
   - Tarayıcınızda YouTube Music'e giriş yapın
   - Cookie bilgilerinin güncel olduğundan emin olun

3. Şarkılar bulunamıyorsa:
   - YouTube Music'te manuel olarak arayın
   - Şarkının farklı bir versiyonunu veya ismini deneyin

## Karşılaşılan Hatalar ve Çözümleri

1. YouTube Music 404 Hatası:
   - **Hata**: YouTube Music API'si 404 "Not Found" hatası döndürüyor
   - **Çözüm**: 
     1. Chrome tarayıcısında YouTube Music'e giriş yapın
     2. Developer Tools'u açın (F12 veya Cmd+Option+I)
     3. Network sekmesine gidin
     4. Sayfayı yenileyin ve cookie değerlerini kopyalayın
     5. `ytmusic_headers.json` dosyasındaki cookie değerini güncelleyin

2. Spotify Yetkilendirme Hatası:
   - **Hata**: Spotify API'sine erişim sağlanamıyor
   - **Çözüm**:
     1. Spotify Developer Dashboard'dan yeni bir uygulama oluşturun
     2. Client ID ve Client Secret'ı yenileyin
     3. `config.json` dosyasını güncelleyin
     4. `auth_spotify.py` scriptini çalıştırın

3. Selenium WebDriver Hatası:
   - **Hata**: Chrome WebDriver bulunamıyor veya çalıştırılamıyor
   - **Çözüm**:
     1. Chrome tarayıcısının en son sürümünü yükleyin
     2. ChromeDriver'ı manuel olarak indirin ve PATH'e ekleyin
     3. Selenium'u pip ile yeniden yükleyin: `pip install selenium --upgrade`

4. Playlist Oluşturma Hatası:
   - **Hata**: YouTube Music'te playlist oluşturulamıyor
   - **Çözüm**:
     1. Cookie değerlerinin tam ve doğru olduğundan emin olun
     2. Authorization header'ını `ytmusic_headers.json` dosyasına ekleyin
     3. YouTube Music hesabınızın aktif olduğunu kontrol edin

