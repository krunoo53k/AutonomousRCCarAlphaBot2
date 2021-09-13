import socket

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print("Socket Up and running with a connection from",addr)
str_input="s"

while True:
    str_input=input("Koji smjer?: ")
    c.send(str_input.encode())
    if str_input == "Bye" or str_input == "bye":
        break
c.close()
