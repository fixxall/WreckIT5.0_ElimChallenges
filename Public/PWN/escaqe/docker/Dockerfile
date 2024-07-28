FROM python:3.7.2-stretch

COPY sources.list /etc/apt/sources.list

RUN apt-get update && apt-get install -y socat lsof && apt-get install -y curl && apt-get install -y wget && apt-get install -y gzip && apt-get install -y qemu-system-x86 && apt-get install -y cpio  && apt-get install -y xinetd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*

RUN mkdir /tmp/fak
RUN useradd -U -m -s /bin/bash ctf
RUN useradd -U -m -s /bin/bash jimbo
RUN chown ctf:ctf /tmp/fak
COPY ./flag.txt /root/flag.txt

COPY ./xinetd.conf /etc/xinetd.conf
RUN chmod 644 /etc/xinetd.conf

COPY ./bzImage /home/jimbo/bzImage
COPY ./launch.sh /home/jimbo/launch.sh
COPY ./xinetd /etc/xinetd.d/xinetd
COPY ./startchall.sh /usr/bin/startchall
COPY ./transfer_file.sh /usr/bin/transferfile
COPY ./initramfs.cpio.gz /home/jimbo/initramfs.cpio.gz
COPY ./ynetd /bin/ynetd

RUN chmod 777 /bin/ynetd
RUN chmod 500 /usr/bin/transferfile
RUN chmod 500 /etc/xinetd.d/xinetd && chmod 500 /usr/bin/startchall && chmod 500 /home/jimbo/launch.sh
RUN chown -R jimbo:jimbo /home/jimbo
RUN su -l ctf -c "ln /dev/null ~/.bash_history -sf"
CMD ["/usr/bin/startchall"]
