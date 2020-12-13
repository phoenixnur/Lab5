import socket
import touch
from Crypto.Cipher import AES

def encrypt(encrypt_data):
        obj = AES.new(b"1122334456789001" , AES.MODE_CFB, b"2299225510784791")
        data = obj.encrypt(encrypt_data)
        return data

def decrypt(decrypt_data):
        obj = AES.new(b"1122334456789001" , AES.MODE_CFB, b"2299225510784791")
        data = obj.decrypt(decrypt_data)
        return data


s = socket.socket()

port = 9898

print("\n server is listening on port: ", port, "\n")

s.bind(('', port))

s.listen(10)


while True:
    conn, addr = s.accept()
    print ("\n connection is accepted from the client!")

    clientFile = conn.recv(1024)
    print ("\n before decryption: " + str(clientFile))
    decrypted = decrypt(clientFile)
    clientFile = decrypted.decode()
    print ("\n after decryption: " + str(clientFile))

    touch.touch(clientFile)
    file = open(clientFile,"wb")

    msg = "\n hello client[ip address: "+ addr[0] + "] \n"

    encrypted = encrypt(msg.encode())
    conn.send(encrypted)

    RecvData = conn.recv(1024)
    temp = decrypt(RecvData)

    while RecvData:
        file.write(temp)

        RecvData = conn.recv(1024)
        temp = decrypt(RecvData)

    file.close()
    print("\n file is stored successfully! ")

    conn.close()
    print("\n the connection is closed \n")

    break
