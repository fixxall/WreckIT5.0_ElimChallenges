FROM debian:12.5-slim

# Set environment variable for root password
ENV ROOT_PASSWORD this_is_not_the_password

# Install dependencies for building OpenSSH
RUN apt-get update && \
    apt-get install -y wget build-essential zlib1g-dev libssl-dev libpam0g-dev && \
    rm -rf /var/lib/apt/lists/*

# Download, compile, and install OpenSSH version 9.7
RUN wget https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-9.7p1.tar.gz && \
    tar -xzf openssh-9.7p1.tar.gz && \
    cd openssh-9.7p1 && \
    ./configure && \
    make && \
    make install && \
    cd .. && \
    rm -rf openssh-9.7p1.tar.gz openssh-9.7p1

# Configure root password
RUN echo "root:${ROOT_PASSWORD}" | chpasswd

# Create necessary directories
RUN mkdir /var/run/sshd

# Copy flag file and SSH config
COPY ./flag.txt /var/tmp/flag.txt

# Expose SSH port
EXPOSE 22

# Copy and set permissions for the start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Start SSH service
CMD ["/start.sh"]
