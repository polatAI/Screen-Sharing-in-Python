# Python ile Ekran Paylaşımı (Screen Sharing)

Bu proje, Python kullanarak yerel ağ üzerinden ekran paylaşımı yapmanızı sağlar. `vidstream` kütüphanesini kullanarak bir cihazdan diğerine gerçek zamanlı ekran aktarımı gerçekleştirilir.

## Özellikler

- 📺 Gerçek zamanlı ekran paylaşımı
- 🌐 Yerel ağ üzerinden düşük gecikmeli yayın
- 🔄 Sunucu ve istemci desteği
- 🚀 Hafif ve kullanımı kolay

## Kurulum

### Gereksinimler
- Python 3.x
- `vidstream` kütüphanesi

### Kurulum Adımları
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/kullaniciadi/screen-sharing-python.git
   cd screen-sharing-python
   ```
2. Gerekli kütüphaneleri yükleyin:
   ```bash
   pip install vidstream
   ```

## Kullanım

### Alıcı (Receiver) Çalıştırma
Alıcı, ekranı görüntüleyen cihazdır.
```bash
python receiver.py
```

### Gönderici (Sender) Çalıştırma
Gönderici, ekranını paylaşan cihazdır.
```bash
python sender.py
```

**Not:** `receiver.py` ve `sender.py` dosyalarında kendi IP adresinizi girmeniz gerekmektedir.

## Örnek Kodlar
### Receiver (Ekran İzleyici)
```python
from vidstream import StreamingServer
import threading

receiver = StreamingServer("192.168.1.114", 9999) # Alıcı IP adresinizi girin

t = threading.Thread(target=receiver.start_server)
t.start()

while input(" ") != "STOP":
    continue

receiver.stop_server()
```

### Sender (Ekran Paylaşan)
```python
from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient("192.168.1.114", 9999) # Alıcı IP adresini girin

t = threading.Thread(target=sender.start_stream)
t.start()

while input(" ") != "STOP":
    continue

sender.stop_stream()
```


## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır.
