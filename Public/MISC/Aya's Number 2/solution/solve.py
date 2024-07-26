from pwn import *

io = process(['python3', '../src/chall.py'])

maxNum = 1606938044258990275541962092341162602522202993782792835301376

def getin(x, y):
    io.recvuntil(b'S0? ')
    io.sendline(str(x).encode())
    io.recvuntil(b'S1? ')
    io.sendline(str(y).encode())
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
# x < is r
# y < is odd

# findingX
print(io.recvline())
left = 1
right = maxNum
while True:
    mid = (left+right)//2
    hasil = getin(mid, 0)
    symbol = hasil[-1:]
    if(symbol==b'\t'):
        right = mid
    elif(symbol==b'\r'):
        left = mid+1
    else:
        print("found X:",mid)
        foundX = mid
        break

# findingY
left = 1
right = maxNum
while True:
    mid = (left+right)//2
    hasil = getin(0, mid)
    cnt_r = hasil.count(b"\r")
    if(cnt_r%2==1):
        left = mid+1
    elif(cnt_r==0):
        print("found Y:",mid)
        foundY = mid
        break
    else:
        right = mid

temp = getin(foundX, foundY)
print(temp)
mod = 1000000000000000009

from fibo import fibo
io.recvuntil(b'S[1]=S1?')
nil = fibo(foundX, foundY, mod)
print(nil)
io.sendline(str(nil).encode())
flag = io.recvline()
print(flag)