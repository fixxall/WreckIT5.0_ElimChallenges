from scapy.all import *

def solve_pcap(filename):
    pkts = rdpcap(filename)  # Read packets from PCAP file

    ascii_text = ''
    for pkt in pkts:
        if TCP in pkt and Raw in pkt:
            data_len = len(pkt[Raw].load)  # Get length of raw payload
            ascii_char = chr(data_len)     # Convert length to ASCII character
            ascii_text += ascii_char       # Append ASCII character to string

    print(f"flag {filename}:")
    print(ascii_text)

if __name__ == "__main__":
    solve_pcap("chall.pcap")

#WRECKIT50{l3ngth_of_th_pack3t?}