from secret import FLAG
from Crypto.Util.number import *
import random

i_have_secret_contd = b'Im READY for SECURITY buzzing MAKE me '+random.randbytes(20)
secretInt = bytes_to_long(i_have_secret_contd)

RSAfuzzingP = getPrime(1024)
RSAfuzzingQ = getPrime(1024)
RSAfuzzingN = RSAfuzzingP*RSAfuzzingQ
RSAfuzzinge = (secretInt*2020202202020220)*getPrime(1024) | 1
while True:
    try:
        RSAfuzzingd = pow(RSAfuzzinge, -1, (RSAfuzzingP-1)*(RSAfuzzingQ-1))
        break
    except:
        RSAfuzzinge += 2

assert pow(secretInt, RSAfuzzinge*RSAfuzzingd, RSAfuzzingN) == secretInt