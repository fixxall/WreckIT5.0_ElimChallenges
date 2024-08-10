FROM ubuntu:23.10

RUN apt-get update && apt-get install -y socat
RUN useradd -UM bypass

COPY bypass /home/bypass/bypass
COPY flag.txt /home/bypass/flag.txt
COPY run.sh /home/bypass/run.sh
RUN chown bypass:bypass /home/bypass/flag.txt && chmod 644 /home/bypass/flag.txt
USER bypass

WORKDIR /home/bypass
EXPOSE 10202
CMD /home/bypass/run.sh
