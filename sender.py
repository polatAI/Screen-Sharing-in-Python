#192.168.1.114
from vidstream import ScreenShareClient
import threading

sender = ScreenShareClient("ip", 9999) # gönderici ip adresini giriniz...

t = threading.Thread(target=sender.start_stream())
t.start()

while input(" ") != "STOP":
    continue

sender.stop_stream()

