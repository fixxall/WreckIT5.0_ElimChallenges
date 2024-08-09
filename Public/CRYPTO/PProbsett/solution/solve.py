from pwn import *
from sage.all import Integer, GF, PolynomialRing, Zmod, matrix
from Crypto.Util.number import long_to_bytes, bytes_to_long
import hashlib
import random

io = process(["python3","../src/chall.py"])

io.recvuntil(b'cipher_number: ')
cip_num = int(io.recvline().decode().strip())
io.recvuntil(b'pub_value: ')
pub_val = [int(i) for i in io.recvline().decode().strip()[1:-1].split(',')]
RSAfuzzinge, RSAfuzzingN = pub_val[0], pub_val[1]

# interaction
def getFlag(ans):
    io.recvuntil(b']: ')
    io.sendline(b'1')
    io.recvuntil(b'answer: ')
    io.sendline(ans)
    flag = io.recvline().decode().strip()
    return flag

def getPublic():
    io.recvuntil(b']: ')
    io.sendline(b'3')
    io.recvuntil(b'p: ')
    p = int(io.recvline().decode().strip())
    io.recvuntil(b'n: ')
    n = io.recvline().decode().strip()
    io.recvuntil(b'e: ')
    e = int(io.recvline().decode().strip())
    return p, n, e

def enc(message):
    io.recvuntil(b']: ')
    io.sendline(b'2')
    io.recvuntil(b'message: ')
    io.sendline(message)
    io.recvuntil(b'ciphertext: ')
    cipher = io.recvline().decode().strip()[1:-1].split(',')
    io.recvuntil(b'signature: ')
    sign = int(io.recvline().decode().strip(),16)
    return cipher, sign

def getNonce(part_secret, part_selfkey):
    io.recvuntil(b']: ')
    io.sendline(b'4')
    io.recvuntil(b'secretCode: ')
    io.sendline(part_secret)
    io.recvuntil(b'selfKey: ')
    io.sendline(part_selfkey)
    io.recvuntil(b'enc_nonce: ')
    return int(io.recvline().decode().strip())

# dec polynomial rsa
def decPoly(p, n, e, c, parser):
    R = GF(p)['x']
    n = R(n)
    c0 = R(c[0])
    for set1 in range(5, 9):
        for set2 in range(5, 9):
            teta = (p**set1-1)*(p**set2-1)
            try:
                d = pow(e, -1, teta)
                plain = pow(c0, d, n)
                if(plain.degree()==1):
                    plainbytes = long_to_bytes(int(plain[0]))
                    if(b'Im READY' in plainbytes):
                        plaintext = plainbytes + b''.join([long_to_bytes(int(pow(R(c[i]), d, n)[0])) for i in range(1, len(c))])
                        return plaintext.split(parser)[0].decode()
            except:
                pass
    print("Not Found")
    return None

# simple HNP
def pad(message):
    return message + b'\x00'*(32 - (len(message)%32))

def attackHNP(iv, p, sized):
    sg = []
    mul = []
    for i in range(1,sized+1):
        temp = str(random.randint(0,1000)).encode()
        mess = pad(iv.encode()+temp)
        c,s = enc(temp)
        R = GF(p)['x']
        c = [R(i) for i in c]
        buff = int(hashlib.sha256(str(c).encode()).hexdigest(),16) 
        digest = int(hashlib.sha256(mess).hexdigest(),16)
        sg.append(s)
        mul.append(buff*digest)
        print("Adding #",i,":",mess[:50])
    return hnpLLL(p, sized, sg, mul)

def hnpLLL(p, sized, sg, mul):
    Zn = Zmod(p)
    B = 2**500
    m = [[0]*i+[p]+[0]*(sized-1-i)+[0,0] for i in range(sized)]
    m += [mul+[B/p,0]]
    m += [sg+[0,B]]
    Mat = matrix(m)
    lll = Mat.LLL()
    for row in lll:
        if row[-1] == B:
            result = Zn(row[-2]*p/B)
            return result

    print("LLL not found number")
    return None

# franklinreiter attacks
def gcd(a, b): 
    while b:
        a, b = b, a % b
    return a.monic()

def franklinreiter(C1, C2, e, N, b, c):
    X = PolynomialRing(Zmod(N),names="X").gen()
    g1 = (X + b)**e - C1
    g2 = (X + c)**e - C2
    result = -gcd(g1, g2).coefficients()[0]
    return int(hex(int(result))[2:].replace("L",""),16)

def main():
    # i_have_secret_contd = f'Im READY for SECURITY code: {secretCode[:40]} buzzing MAKE me code: {secretCode[40:]}'.encode()
    p, n, e = getPublic()
    plain = b"message"
    c1, s1 = enc(plain)
    iv = decPoly(p, n, e, c1, plain)
    first_part_code = iv.split('code: ')[1]
    print("Getting firs_part:",first_part_code)
    inc = 60
    selfk = attackHNP(iv, Integer(p), inc)
    print("Getting selfk:",selfk)
    selfKey = hashlib.sha256(long_to_bytes(int(selfk))).hexdigest()
    enc_nonce1 = getNonce(first_part_code[:10].encode(), selfKey[:10].encode())
    c2, s2 = enc(plain)
    enc_nonce2 = getNonce(first_part_code[:10].encode(), selfKey[:10].encode())
    nonce = franklinreiter(enc_nonce1, enc_nonce2, 5, RSAfuzzingN, inc+1, inc+2)
    print("Getting nonce:",nonce)
    RSAfuzzingd = int(int(nonce)) * int(p) + int(selfk)
    secret_contd = long_to_bytes(int(pow(cip_num, int(RSAfuzzingd), RSAfuzzingN)))
    # print(secret_contd)
    flag = getFlag(secret_contd)
    print(flag)

main()
io.close()
