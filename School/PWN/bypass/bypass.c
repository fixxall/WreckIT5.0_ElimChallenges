#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h> 
#include <string.h>

void __attribute__((constructor)) setup()
{
  setvbuf(stdin, 0, _IONBF, 0);
  setvbuf(stdout, 0, _IONBF, 0);
  setvbuf(stderr, 0, _IONBF, 0);
}

void apatuh(void) {
  system("cat flag.txt");
}
int main(int argc, char **argv, char **envp)
{
  printf("Passwordnya: ");
  char buf[3]; 
  char s2[6] = "apayah";
  read(0, buf, 4);
  if ( !strcmp(buf, s2) )
    apatuh();
  else
    fprintf(stderr, "Masih belum...\n");
    exit(0);
  return 0;
}
