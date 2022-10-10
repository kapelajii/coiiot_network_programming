import socket

HOST = "127.0.0.1"
PORT = 10001

# Let's set up a server that uses the AF_INET address family and the TCP protocol
tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# let's bind the server to the IP address and port given above
tcp_server.bind((HOST,PORT))

# Listen specifies the number of unaccepted connections that the system will allow before refusing new connections
tcp_server.listen(5)
print("Server running...")

while True:
  communication_socket, address = tcp_server.accept()
  print(f"connected to client:  {address}")
  data_from_client = communication_socket.recv(1024).decode('utf-8')
  print(f"Data from client: {data_from_client}")
   # Response message to client
  communication_socket.send("OK".encode('utf-8'))
  
  communication_socket.close()
  print(f"connection with client {address} closed")
