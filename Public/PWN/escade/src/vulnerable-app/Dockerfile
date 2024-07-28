FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    gcc \
    netcat \
    socat

# Copy vulnerable binary
COPY vulnerable.c /home/vulnerable.c
COPY compile.sh /home/compile.sh
RUN chmod +x /home/compile.sh && /home/compile.sh

# Set up entrypoint
CMD ["socat", "TCP-LISTEN:8080,fork,reuseaddr", "EXEC:/home/vulnerable"]
