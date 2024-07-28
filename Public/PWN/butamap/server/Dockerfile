#FROM debian:stretch
FROM python:3.7.2-stretch

COPY sources.list /etc/apt/sources.list
RUN apt-get update && apt-get install -y qemu-system-x86 && apt-get install -y lsof && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN useradd -U -m -s /bin/bash ctf

WORKDIR /home/ctf

COPY ./bzImage /home/ctf/bzImage
COPY ./initramfs.cpio.gz /home/ctf/initramfs.cpio.gz
COPY ./launch.sh /home/ctf/launch.sh
COPY ./ynetd /usr/bin/ynetd

RUN chmod +x /usr/bin/ynetd
RUN chmod 500 /home/ctf/launch.sh && chown -R ctf:ctf /home/ctf && touch /var/log/challog.txt && chown ctf:ctf /var/log/challog.txt

CMD ["/usr/bin/ynetd", "-lt", "28800", "-p", "16968", "-sh", "y", "/home/ctf/launch.sh"]
