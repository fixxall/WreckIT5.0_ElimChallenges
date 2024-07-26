#!/usr/bin/python3
import base64

def xor(data):
    hasil = []
    for i, val in enumerate(data):
        shifted = (val ^ i) << (i % 8) | (val ^ i) >> (8 - (i % 8))
        hasil.append(shifted & 0xFF) 
    return hasil

if __name__ == '__main__':
    result_str = "WRECKIT50{b4by_pyth0n_c0mp1led_c0d3}"
    
    enc = base64.b64encode(result_str.encode()).decode()
    mis_pad = len(enc) % 4
    if mis_pad:
        enc += '=' * (4 - mis_pad)
    dec = base64.b64decode(enc)
    hasil = xor(dec)
    print(hasil)
