import socket

serverip = "192.168.1.7"

s = socket.socket()
s.connect((serverip, 12345))

while True:
