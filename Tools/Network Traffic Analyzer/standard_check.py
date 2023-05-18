import dpkt
import socket


def parse_packet(packet):
    eth = dpkt.ethernet.Ethernet(packet)  # Parse the Ethernet frame
    ip = eth.data  # Get the IP packet from the Ethernet frame

    # Extract relevant information from the IP packet
    src_ip = socket.inet_ntoa(ip.src)
    dst_ip = socket.inet_ntoa(ip.dst)

    if isinstance(ip.data, dpkt.tcp.TCP):
        tcp = ip.data  # Get the TCP segment from the IP packet
        src_port = tcp.sport
        dst_port = tcp.dport
        protocol = 'TCP'
    elif isinstance(ip.data, dpkt.udp.UDP):
        udp = ip.data  # Get the UDP datagram from the IP packet
        src_port = udp.sport
        dst_port = udp.dport
        protocol = 'UDP'
    else:
        src_port = None
        dst_port = None
        protocol = 'Other'

    # Perform your analysis and threat detection logic here
    print(
        f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}")
    if src_port and dst_port:
        print(f"Source Port: {src_port}, Destination Port: {dst_port}")


def packet_handler(packet):
    try:
        parse_packet(packet)
    except dpkt.dpkt.UnpackError:
        pass  # Ignore malformed packets


# Sniff packets on the network interface
sniff(prn=packet_handler, filter="tcp or udp", count=10)
