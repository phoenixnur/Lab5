import socket

s = socket.socket(family = socket.AF_INET, type=socket.SOCK_DGRAM)
print("berjaya buat socket")

port = 8888

s.bind(("",port))
print("berjaya bind socket di port: " + str(port))

#s.listen(5)
print("soket tengah menunggu client!")

while True:

	c = s.recvfrom(1024)
	msg = c[0]
	addr = c[1]
	print("dapat capaian dari: " + str(addr))

	s.sendto(b'terima kasih!',addr)
	print(msg)

c.close()
