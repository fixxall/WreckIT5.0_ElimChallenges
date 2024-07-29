#!/bin/bash
gcc -m32 -fno-stack-protector -z execstack -o /home/vulnerable /home/vulnerable.c
