# This is a TCP client providing simple methods for connecting, 
# sending, and receiving stream data over a network in synchronous blocking mode.
import socket

target_host = "www.google.com"
target_port = 80

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect(target_host, target_port)

#send some data
client.send(b"GET / HTTP/1.1\r\nHost:google.com\r\n\r\n")

#recieve some data
dataresponse = client.recv(4096)

print(response.decode())
client.close()