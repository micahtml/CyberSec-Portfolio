import dpkt
import socket
import scapy
from scapy.all import sniff


def parse_packet(packet):
    eth = dpkt.ethernet.Ethernet(packet)  # Parse the Ethernet frame
    ip = eth.data  # Get the IP packet from the Ethernet frame

    if isinstance(ip.data, dpkt.tcp.TCP):
        tcp = ip.data  # Get the TCP segment from the IP packet
        payload = tcp.data

        # Perform analysis and threat detection on the payload
        if len(payload) > 0:
            suspicious_keywords = ['password', 'admin', 'malware', 'hack']
            for keyword in suspicious_keywords:
                if keyword.encode() in payload:
                    print("Suspicious payload detected!")
                    print(
                        f"Source IP: {socket.inet_ntoa(ip.src)}, Destination IP: {socket.inet_ntoa(ip.dst)}")
                    print(f"Payload: {payload.decode()}")
                    break


def packet_handler(packet):
    try:
        parse_packet(packet)
    except dpkt.dpkt.UnpackError:
        pass  # Ignore malformed packets


# Sniff packets on the network interface
sniff(prn=packet_handler, filter="tcp", count=10)
