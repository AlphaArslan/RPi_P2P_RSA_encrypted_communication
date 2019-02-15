import socket

my_ip  = "192.168.1.6"
his_ip = "192.168.1.5"
port   = 2124

s = socket.socket()
s.bind((my_ip, port))
s.listen(1)

conn, addr = s.accept()

print "connected to : ", addr

while 1:
	data = conn.recv(1024)
	if not data: break
	print("->"+data)

conn.close()
