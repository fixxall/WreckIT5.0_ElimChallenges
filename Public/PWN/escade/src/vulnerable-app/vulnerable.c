#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void shell() {
    system("/bin/sh");
}

void vuln() {
    char buffer[64];
    printf("Enter some text: ");
    gets(buffer); // Vulnerable to buffer overflow
    printf("You entered: %s\n", buffer);
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    vuln();
    return 0;
}
