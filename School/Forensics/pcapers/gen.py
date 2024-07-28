import random
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.http import Raw

def generate_pcap(filename, input_string):
    packets = []
    ip = "127.0.0.1"

    for char in input_string:
        payload_length = ord(char)
        payload = b'A' * payload_length
        port = random.randint(1024, 65535)
        sport = random.randint(1024, 65535)
        seq = random.randint(0, 10000)
        
        # Create a TCP SYN packet
        syn = IP(dst=ip) / TCP(dport=port, sport=sport, flags="S", seq=seq)
        packets.append(syn)
        
        # Create a TCP SYN/ACK response
        syn_ack = IP(dst=ip) / TCP(dport=sport, sport=port, flags="SA", seq=random.randint(0, 10000), ack=seq + 1)
        packets.append(syn_ack)
        
        # Create a TCP ACK packet
        ack = IP(dst=ip) / TCP(dport=port, sport=sport, flags="A", seq=seq + 1, ack=syn_ack[TCP].seq + 1)
        packets.append(ack)
        
        # Create a TCP packet with the payload
        tcp_payload = IP(dst=ip) / TCP(dport=port, sport=sport, flags="PA", seq=ack[TCP].seq, ack=ack[TCP].ack) / Raw(load=payload)
        packets.append(tcp_payload)
        
        # Create a TCP ACK for the payload
        ack_payload = IP(dst=ip) / TCP(dport=port, sport=sport, flags="A", seq=tcp_payload[TCP].seq + len(payload), ack=tcp_payload[TCP].ack)
        packets.append(ack_payload)
    
    # Write packets to PCAP file
    wrpcap(filename, packets)
    print(f"PCAP file {filename} generated successfully with packets based on the string '{input_string}'.")

if __name__ == "__main__":
    input_string = "YWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFiYmJiYmJiYmJiYmJiYmJiYmJiYmJiYmJiYmNjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NkZGRkZGRkZGRkZGRkZGR+V1JFQ0tJVDUwe2wzbmd0aF9vZl90aF9wYWNrM3Q/fX5hYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWFhYWJiYmJiYmJiYmJiYmJiYmJiYmJiYmJiYmJiY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2RkZGRkZGRkZGRkZGRkZA=="
    generate_pcap("chall.pcap", input_string)
