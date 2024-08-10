#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

void apanih(void) {
  system("/bin/sh");
}

int main(void) {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stdout, NULL);
  srand(time(NULL));
  char buffer[72];
  puts("tut");
  while (1) {
    fgets(buffer, 128, stdin);
    char *s = strstr(buffer, "aku");
    if (s) {
      printf("uuuuuuuu", s + 8);
    } else if (strcmp(buffer, "yyyyyyyy") == 0) {
      puts("aaaaaa");
      sleep(5);
      puts("bbbbb");
    } else if (strcmp(buffer, "nyerah") == 0) {
      puts("heeeeeeeeeeee");
      break;
    } else {
      puts("hohohihhe");
    }
  }
}
