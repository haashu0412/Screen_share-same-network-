from vidstream import StreamingServer
import threading

receiver = StreamingServer('#ip_add',9999)

t = threading.Thread(target=receiver.start_server)
t.start()

while input("") != 'STOP':
    continue

receiver.stop_server()




