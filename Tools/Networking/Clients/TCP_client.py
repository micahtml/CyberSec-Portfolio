# This is a TCP client providing simple methods for connecting, 
# sending, and receiving stream data over a network in synchronous blocking mode.
import socket

target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the target host and port
# Corrected syntax for the connect method
client.connect((target_host, target_port))

# Send some data
# Added a space after the colon in the Host header
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

# Receive some data
dataresponse = client.recv(4096)

# Print the received data
# Changed the variable name from 'response' to 'dataresponse'
print(dataresponse.decode())

# Close the socket connection
client.close()
