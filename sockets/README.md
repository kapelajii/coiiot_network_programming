# Sockets

## Basics

**Server**
is computer software that waits for customer service requests. The server responds to the client's requests by offering services or resources. Process takes action only when asked to do something on behalf of a client

**client**
active party that generates request, send them to a server and does something with the result that it gets back

**Protocol**
the language or set of rules how client and server communicate between each other. Servers and clients must use a common protocol to understand each other

![image](img/socket_image_1.png)

**Course book**

[Stevens W. R., Fenner B., Rudolf A.M: UNIX Network Programming, Volume 1, 3rd Edition , Addison Wesley, 2004. The course covers the chapters 1-8, 11-17, 20-26 and 30 plus Appendixes A-D of the course book.](https://github.com/sqm2050/wiki/blob/master/Books/c%26programme/UNIX%20Network%20Programming%2C%20Volume%201%2C%20Third%20Edition%2C%20The%20Sockets%20Networking%20API.pdf)



## Socket

- A socket is a communications connection point (endpoint) that you can name and address in a network. 
- Endpoint consists of an IP address and a port number 

```
[IP ADDRESS]: [PORT NUMBER]
EXAMPLE: 192.168.100.55:8190
```
- Sockets are commonly used for client and server interaction. Typical system configuration places the server on one machine, with the clients on other machines. The clients connect to the server, exchange information, and then disconnect.

## IP Address and port

- Socket connection uses the TCP protocol for communication
- IP address identifies the computer in the network
- Port identifies the application or service running on the computer

![image](img/socket_image_2.png)


```
Commonly used ports:

FTP (File tranfer) port 21
SSH (secure shell) port 22
TELNET port 23
SMTP (e-mail) port 25             
DNS port 53
HTTP port 80
HTTPS (secure web browsing) port 443

```
[IANA.ORG -List of registered port numbers](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)

## Socket communication

**Client setup**
1. Connect to same network with server
2. Look up the address of a server
3. Create client socket
4. Connect to the server using ip address and port

**Server setup**
1. Create socket server
2. Setup socket server
3. Bind created socket to spesific port
4. Listen for new connections from clients
5. Accept new connections


![image](img/socket_image_3.png)
TCP Socket flow

## Python socket

### Client socket

Create new socket communication using host and port

```python
import socket

HOST = '127.0.01'
PORT = 8190

```

