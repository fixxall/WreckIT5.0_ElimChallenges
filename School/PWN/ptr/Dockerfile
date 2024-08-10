FROM ubuntu:22.04

RUN apt-get update && apt-get install -y socat
RUN useradd -UM introtoptr

COPY introtoptr /home/introtoptr/introtoptr
COPY flag.txt /home/introtoptr/flag.txt
COPY run.sh /home/introtoptr/run.sh
RUN chown introtoptr:introtoptr /home/introtoptr/flag.txt && chmod 644 /home/introtoptr/flag.txt
USER introtoptr

WORKDIR /home/introtoptr
EXPOSE 10201
CMD /home/introtoptr/run.sh
