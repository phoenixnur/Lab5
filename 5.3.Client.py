import socket
import sys
import json

s = socket.socket()

port = 8080

s.connect(('192.168.0.162', port))

data = s.recv(1024)
data = data.decode('utf-8')

s.send(b'thank you from client!')

dataJ = json.loads(data)

print(type(dataJ))

s.close()
