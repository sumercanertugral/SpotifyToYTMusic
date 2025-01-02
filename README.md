# Spotify'dan YouTube Music'e Şarkı Aktarma Aracı

Bu araç, Spotify'daki beğendiğiniz şarkıları veya çalma listelerinizi YouTube Music'e otomatik olarak aktarmanızı sağlar.

## Özellikler

- ✨ Spotify'daki beğenilen şarkıları YouTube Music'e aktarma
- 📝 Özel çalma listelerini aktarma
- 🔍 Akıllı şarkı eşleştirme algoritması
- 📊 Detaylı loglama sistemi
- 🚀 Hata toleranslı çalışma (bulunamayan şarkıları atlayıp devam eder)
- 🔄 Kesintisiz aktarım süreci
- 🍪 cookie.png
## Gereksinimler

- Python 3.6 veya üzeri
- pip (Python paket yöneticisi)
- Spotify hesabı
- YouTube Music hesabı
- Chrome tarayıcısı

## Kurulum

1. Projeyi bilgisayarınıza indirin:
```bash
git clone https://github.com/sumercanertugral/SpotifyToYTMusic.git
cd SpotifyToYTMusic
```

2. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

## Kullanmadan Önce Kontrol Edilmesi Gerekenler

1. YouTube Music'te aynı isimde başka bir çalma listesinin olmadığından emin olun
2. Spotify'da aktarmak istediğiniz çalma listesinin ID'sini hazırlayın
   - Spotify'da çalma listesine gidin
   - Share > Copy link to playlist'e tıklayın
   - Linkteki ID'yi kopyalayın (örn: spotify.com/playlist/5LI3TG6Yfp7dbud9R5hsj9)
3. İnternet bağlantınızın stabil olduğundan emin olun
4. Yeterli disk alanınızın olduğundan emin olun (loglar için)

## Kullanım

1. Programı çalıştırın:
```bash
python3 runLocally.py
```

2. Menüden yapmak istediğiniz işlemi seçin:
   - 1: Beğenilen şarkıları aktar
   - 2: Özel playlist aktar
   - 3: Çıkış

3. Seçiminize göre gerekli bilgileri girin:
   - Beğenilen şarkılar için: Otomatik olarak aktarılacaktır
   - Özel playlist için: Spotify playlist ID'si ve YouTube Music'te oluşturulacak playlist adını girin

## Algoritma Çalışma Mantığı

1. Spotify API üzerinden şarkı bilgileri alınır
2. Her şarkı için:
   - Şarkı adı ve sanatçı bilgisi YouTube Music'te aranır
   - En uygun eşleşme bulunur ve yeni playlist'e eklenir
   - Bulunamayan veya özel karakter içeren şarkılar loglanır
   - İşlem kesintisiz devam eder

## Loglama Sistemi

Program iki farklı log dosyası oluşturur:
- `logs/transfer_TARIH.log`: Genel işlem logları
- `logs/failed_songs_TARIH.log`: Aktarılamayan şarkıların listesi

## Hata Durumları

1. Şarkı Bulunamadı: 
   - Log dosyasına kaydedilir
   - İşlem diğer şarkılarla devam eder

2. Bağlantı Hataları:
   - Otomatik olarak yeniden denenir
   - Başarısız olursa log dosyasına kaydedilir

3. Yetkilendirme Hataları:
   - Kullanıcıya bilgi verilir
   - Yeniden giriş yapması istenir

4. Cookie Hataları:
   - "401 Unauthorized" hatası alırsanız cookie'niz geçersiz olmuş olabilir
   - Cookie alma adımlarını tekrarlayın
   - Yeni cookie ile tekrar deneyin

## Sık Karşılaşılan Sorunlar

1. "404 Not Found" Hatası:
   - Cookie bilgilerinizi kontrol edin
   - YouTube Music hesabınızın aktif olduğundan emin olun
   - Playlist adının uygun olduğundan emin olun

2. "401 Unauthorized" Hatası:
   - Cookie'niz geçersiz olmuş olabilir
   - Cookie alma adımlarını tekrarlayın
   - Yeni cookie ile tekrar deneyin

3. Şarkı Bulunamama Durumu:
   - Şarkı adı veya sanatçı adı farklı yazılmış olabilir
   - YouTube Music'te manuel olarak arayıp kontrol edin
   - Log dosyasından hangi şarkıların bulunamadığını görebilirsiniz

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: X eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun


## İletişim

Sümer Can Ertuğral - [GitHub](https://github.com/sumercanertugral)

