import socket

s=socket.socket()

 
port = 8888

s.connect (('192.168.0.162',port))

data = s.recv(1024)

s.send(b'hi, saya client. terima kasih!');

print(data)

s.close()
