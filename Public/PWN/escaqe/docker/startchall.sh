#!/bin/sh

socat TCP-LISTEN:7125,reuseaddr,fork EXEC:"/usr/bin/transferfile" &
#/etc/init.d/xinetd start;
/bin/ynetd -lt 28000 -p 7126 -sh y /home/jimbo/launch.sh
sleep infinity;

