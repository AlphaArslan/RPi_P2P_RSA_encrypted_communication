################### IMPORT
import socket

################### Global Variables
my_ip = "192.168.1.5"
his_ip = "192.168.1.6"
port = 2124
msg = ""
s = socket.socket()

################### Function
def getpublickey():
    pubKey = tuple(map(int,input("Enter publicKey q, n : ").split(',')))
    return pubKey

def RSAencrypt(data):
    return data

################### SETUP
s.bind((my_ip,port))
s.connect((his_ip, port))

################### Main


while True:
    #get text from user and encrypt it
    msg = input("-> ")
    s.sendall(msg.encode('utf-8'))


s.close()
s.detach()
