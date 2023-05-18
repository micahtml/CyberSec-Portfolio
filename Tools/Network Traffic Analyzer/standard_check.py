from scapy.all import *


def packet_handler(packet):
    # Process the packet here
    print(packet.summary())


# Sniff packets on the network interface
sniff(prn=packet_handler, filter="tcp or udp", count=10)
