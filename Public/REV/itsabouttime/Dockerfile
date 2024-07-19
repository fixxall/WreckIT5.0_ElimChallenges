# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set environment variables
ENV USER=ctfuser
ENV HOME=/home/$USER

# Install necessary packages
RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo

# Create a user and set up SSH
RUN useradd -m -d $HOME -s /bin/bash $USER && \
    echo "$USER:$USER" | chpasswd && \
    mkdir -p $HOME/.ssh && \
    chown -R $USER:$USER $HOME/.ssh && \
    chmod 700 $HOME/.ssh

# Add the public key to authorized_keys
COPY ctfuser_key.pub $HOME/.ssh/authorized_keys
RUN chown $USER:$USER $HOME/.ssh/authorized_keys && \
    chmod 600 $HOME/.ssh/authorized_keys

# Set up SSH server
RUN mkdir /var/run/sshd && \
    echo 'PermitRootLogin no' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

# Add the flag file
COPY flag.txt $HOME/flag.txt
RUN chown $USER:$USER $HOME/flag.txt && \
    chmod 600 $HOME/flag.txt

# Start SSH server
CMD ["/usr/sbin/sshd", "-D"]
