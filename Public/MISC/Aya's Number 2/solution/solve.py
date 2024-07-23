from pwn import *

io = process(['python3', '../src/chall.py'])

def getin(x, y):
    io.recvuntil(b'S0? ')
    io.sendline(str(x).encode())
    io.recvuntil(b'S1? ')
    io.sendline(str(x).encode())
    return io.recvline()[:-1]

# Lab #1
# for i in range(8):
#     hasil = getin(0,0)
#     print(hasil)

# Lab #2
# for i in range(8):
#     hasil = getin(0,16069380442589902755419620923411626025222029937827928353013761)
#     print(hasil)

# Lab #3
# for i in range(8):
#     hasil = getin(16069380442589902755419620923411626025222029937827928353013761,0)
#     print(hasil)

# Lab #4
# for i in range(8):
#     hasil = getin(16069380442589902755419620923411626025222029937827928353013761,16069380442589902755419620923411626025222029937827928353013761)
#     print(hasil)

# Conclusion
# leftTop = odd + r
# leftBottom = even + r
# rightTop = odd + t
# rightBottom = even + t

