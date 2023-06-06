# This is a UDP client that provides simple methods for sending
# and receiving connectionless UDP datagrams in blocking synchronous mode.

import socket

target_host = "127.0.0.1"
target_port = 9997

# create socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto(b"AAAABBBCCC", (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

# print the received data
print(data.decode())

# close the client socket
client.close()
