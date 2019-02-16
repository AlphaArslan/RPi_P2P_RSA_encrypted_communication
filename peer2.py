################### IMPORT
import socket

################### Global Variables
my_ip  = "192.168.1.6"
his_ip = "192.168.1.5"
port   = 2124
s = socket.socket()

################### Function
def getprivatekey():
    privateKey = tuple(map(int,input("Enter publicKey q, n : ").split(',')))
    return privateKey

def RSA_decrypt(text)
	return text

################### Setup
s.bind((my_ip, port))
s.listen(1)
conn, addr = s.accept()
print "connected to : ", addr

################### Main

while 1:
	data = conn.recv(1024)
	if not data: break
	print("->"+data)

conn.close()
