#!/bin/bash

#
# logging
#
date >> /var/log/challog.txt; /usr/bin/lsof -i -n -P | /bin/grep ESTABLISHED >> /var/log/challog.txt; echo -e >> /var/log/challog.txt

#
# launch
#
timeout --foreground 28800 /usr/bin/qemu-system-x86_64 \
	-kernel /home/ctf/bzImage \
	-m 256M \
	-initrd /home/ctf/initramfs.cpio.gz \
	-nographic \
	-monitor none \
	-no-reboot \
	-append "console=ttyS0 kaslr nosmap nosmep nokptiquiet panic=1 oops=panic"
