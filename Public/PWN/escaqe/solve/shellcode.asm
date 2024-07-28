
xor rax, rax
xor rbx, rbx

mov rax, 0xffff88800e446b70
mov rbx, qword [rax]

xor r15, r15
mov qword [rbx], r15
mov qword [rbx+8], r15
mov qword [rbx+16], r15
ret