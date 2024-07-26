#!/usr/bin/python3
import base64

def xor(hasil):
    data = []
    for i, val in enumerate(hasil):
        shifted = (val >> (i % 8) | val << (8 - (i % 8))) & 0xFF
        data.append(shifted ^ i)
    return data

known = [87, 166, 29, 2, 244, 137, 148, 25, 56, 228, 161, 249, 230, 142, 84, 191, 105, 202, 233, 25, 167, 73, 93, 147, 117, 210, 172, 187, 151, 47, 80, 62, 16, 138, 68, 242]
hasil = bytes(xor(known))
print(hasil.decode())

