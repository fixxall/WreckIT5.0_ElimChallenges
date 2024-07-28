FROM debian:12.5-slim

RUN apt-get update && apt-get install -y openssh-server sudo cron && rm -rf /var/lib/apt/lists/*

ARG ROOT_PASSWORD
RUN echo "root:${ROOT_PASSWORD}" | chpasswd

RUN mkdir /var/run/sshd

COPY ./flag.txt /flag.txt

COPY sshd_config /etc/ssh/sshd_config

EXPOSE 22

COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
