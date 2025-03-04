from vidstream import StreamingServer
import threading

receiver = StreamingServer("ip", 9999) # alıcı ip adresini giriniz...

t = threading.Thread(target=receiver.start_server())
t.start()


while input(" ") != "STOP":
    continue

receiver.stop_server()


