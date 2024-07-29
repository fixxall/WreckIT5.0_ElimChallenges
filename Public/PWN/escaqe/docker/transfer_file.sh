#!/bin/bash

/bin/rm -rf /tmp/fak
/bin/mkdir /tmp/fak
/bin/chown ctf:ctf /tmp/fak

/bin/date >> /var/log/challog.txt; /usr/bin/lsof -i -n -P | /bin/grep ESTABLISHED >> /var/log/challog.txt; /bin/echo -e >> /var/log/challog.txt

/bin/su -l ctf -c "bash -i 2>&1"
