import socket

HOST = "127.0.0.1"
PORT = 10001

my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

my_socket.connect((HOST,PORT))

my_socket.send("Hello world".encode('utf-8)'))

data_from_socket = my_socket.recv(1024).decode('utf-8')

print(data_from_socket)
