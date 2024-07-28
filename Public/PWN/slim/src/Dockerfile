FROM debian:slim

RUN apt-get update && apt-get install -y openssh-server sudo && rm -rf /var/lib/apt/lists/*

ARG ROOT_PASSWORD
RUN echo "root:${ROOT_PASSWORD}" | chpasswd

RUN mkdir /var/run/sshd

COPY flag.txt /root/flag.txt
RUN chmod 444 /root/flag.txt && chattr +i /root/flag.txt

COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22

COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
