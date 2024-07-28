# Start with an official Ubuntu base image
FROM ubuntu:latest

# Install required dependencies
RUN apt-get update && \
    apt-get install -y wget software-properties-common && \
    add-apt-repository ppa:costamagnagianfranco/openssh -y && \
    apt-get update

# Install OpenSSH 9.7 and cron
RUN apt-get install -y openssh-server=1:9.7p1-1~ppa1~ubuntu22.04.1 cron

# Create necessary directories
RUN mkdir /var/run/sshd

# Set root password and create a user for SSH
RUN echo 'root:rootpassword' | chpasswd

# Configure SSH to allow root login
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create a user for the challenge
RUN useradd -m ctfuser && echo 'ctfuser:ctfpassword' | chpasswd

# Add the initial flag to the ctfuser's home directory
RUN echo "WRECKIT50{w0w_cv3_hunt3r!!!_n0t_v3ry_c00l_th0ugh}" > /home/ctfuser/flag.txt && chown ctfuser:ctfuser /home/ctfuser/flag.txt

# Add a cron job to update the flag every minute
RUN echo "* * * * * echo 'WRECKIT50{w0w_cv3_hunt3r!!!_n0t_v3ry_c00l_th0ugh}' > /home/ctfuser/flag.txt && chown ctfuser:ctfuser /home/ctfuser/flag.txt" > /etc/cron.d/flag-update

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/flag-update

# Apply the cron job
RUN crontab /etc/cron.d/flag-update

# Expose the SSH port
EXPOSE 22

# Start the SSH and cron services
CMD service cron start && /usr/sbin/sshd -D
