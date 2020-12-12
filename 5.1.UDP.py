import socket

s = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

ServerAdd = ("192.168.0.162", 8888)

s.sendto(b"hi, saya client. terima kasih!", ServerAdd);

data = s.recvfrom(1024)

print(data[0])

s.close()
