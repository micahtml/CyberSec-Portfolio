import pyshark


def parse_packet(packet):
    ip = packet.ip
    src_ip = ip.src
    dst_ip = ip.dst

    if hasattr(packet, 'tcp'):
        transport_layer = packet.tcp
        src_port = transport_layer.srcport
        dst_port = transport_layer.dstport
        protocol = 'TCP'
    elif hasattr(packet, 'udp'):
        transport_layer = packet.udp
        src_port = transport_layer.srcport
        dst_port = transport_layer.dstport
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


capture = pyshark.LiveCapture(interface='eth0', bpf_filter='tcp or udp')
capture.sniff(packet_count=10)
for packet in capture:
    parse_packet(packet)
