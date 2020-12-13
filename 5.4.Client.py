import socket
import sys
from Crypto.Cipher import AES

def encrypt(encrypt_data):
	obj = AES.new(b"1122334456789001" , AES.MODE_CFB, b"2299225510784791")
	data = obj.encrypt(encrypt_data)
	return data

def decrypt(decrypt_data):
        obj = AES.new(b"1122334456789001" , AES.MODE_CFB, b"2299225510784791")
        data = obj.decrypt(decrypt_data)
        return data


serverIP = "192.168.0.162"

s = socket.socket()
port = 9898
s.connect((serverIP, port))

print ("\n connected to the server! ")

loop = 1
while loop == 1:
	userFile = input("\n enter the file name: ")
	try:
		file = open(userFile, "rb")
		loop = -1

		print ("\n before encryption: " + str(userFile) )
		encrypted = encrypt(userFile.encode())
		print ("\n after encryption : " + str(encrypted) )
		s.send(encrypted)

	except IOError:
		print ("\n unable to open file. please try again \n")

SendData = file.read(1024)
while SendData:
	msg = s.recv(1024)
	temp = decrypt(msg)

	print("\n ------------------------ \n ",temp.decode())
	#Sending file

	encrypted = encrypt(SendData)
	s.send(encrypted)

	SendData = file.read(1024)

s.close()
