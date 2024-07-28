#!/usr/bin/python3
from base64 import b64encode as b64e, b64decode as b64d

def xor(data):
    hasil = []
    for i, val in enumerate(data):
        shifted = (val ^ i) << (i % 8) | (val ^ i) >> (8 - (i % 8))
        hasil.append(shifted & 0xFF) 
    return hasil

usr_input = input(">>> ")
usr_input = usr_input.encode()
enc = b64e(usr_input).decode()
mis_pad = len(enc) % 4
if mis_pad:
    enc += '=' * (4 - mis_pad)
dec = b64d(enc)
apani = xor(dec)
apatuh = [87, 166, 29, 2, 244, 137, 148, 25, 56, 228, 161, 249, 230, 142, 84, 191, 105, 202, 233, 25, 167, 73, 93, 147, 117, 210, 172, 187, 151, 47, 80, 62, 16, 138, 68, 242]
if apani == apatuh:
    print('Nais!')
else:
    print('Coba lagi!')
