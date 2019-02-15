import socket

#setup socket
my_ip = "192.168.1.5"
his_ip = "192.168.1.6"
port = 2124
s = socket.socket()
s.bind((my_ip,port))
s.connect((his_ip, port))
msg = ""
while True:
    #get text from user and encrypt it
    msg = input("-> ")
    s.sendall(msg.encode('utf-8'))

#send it to peer2

s.close()
s.detach()
