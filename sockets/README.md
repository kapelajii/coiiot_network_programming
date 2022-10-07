# Sockets

## Basics

**Server**
is computer software that waits for customer service requests. The server responds to the client's requests by offering services or resources. Process takes action only when asked to do something on behalf of a client

**client**
active party that generates request, send them to a server and does something with the result that it gets back

**Protocol**
the language or set of rules how client and server communicate between each other. Servers and clients must use a common protocol to understand each other

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

## Python socket

### Client socket

Create new socket communication using host and port

```python
import socket

HOST = '127.0.01'
PORT = 8190

```

