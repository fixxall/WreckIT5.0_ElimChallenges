//gcc -o chall chall.c -lseccomp -z execstack -s
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <seccomp.h>

void setup_seccomp(int *syscalls) {
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_KILL);

    if (ctx == NULL) {
        perror("seccomp_init");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < 4; i++) {
        seccomp_rule_add(ctx, SCMP_ACT_ALLOW, syscalls[i], 0);
    }

    seccomp_load(ctx);
}

void get_user_input() {
    char v18[92];
    char *buffer; 
    int *syscalls;
    char *v11;
    
    memset(v18, 0, sizeof(v18));
    buffer = v18;
    syscalls = &buffer[80];
    syscalls[0] = SCMP_SYS(write);
    syscalls[1] = SCMP_SYS(exit);
    syscalls[2] = SCMP_SYS(exit_group);
    syscalls[3] = SCMP_SYS(lstat);

    printf("Choose your target: ");
    int buf = read(0, buffer, 0x500);

    for (int i = 0; i < 80; i++) {
        if (buffer[i] == '\0') {
            printf("No cheat allowed!\n");
            exit(1);
        }
    }
    printf("Target confirmed: %s\n", buffer);

    if (strstr(buffer, "HEADSHOT") != NULL) {
        printf("HEADSHOT!. Another chance!.\n");
        get_user_input();
    } else {
        setup_seccomp(syscalls);
        printf("You lose\n");
    }
}

int main() {
	setvbuf(stdout, NULL, 2, 0);
	setvbuf(stdin, NULL, 2, 0);
	setvbuf(stderr, NULL, 2, 0);
    get_user_input();
    return 0;
}
