# Start with an official Ubuntu base image
FROM ubuntu:latest

# Install OpenSSH server
RUN apt-get update && apt-get install -y openssh-server

# Create necessary directories
RUN mkdir /var/run/sshd

# Set root password and create a user for SSH
RUN echo 'root:rootpassword' | chpasswd

# Configure SSH to allow root login
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Create a user for the challenge
RUN useradd -m ctfuser && echo 'ctfuser:ctfpassword' | chpasswd

# Add the flag to the ctfuser's home directory
RUN (crontab -l ; echo "* * * * * echo 'WRECKIT50{w0w_cv3_hunt3r!!!_n0t_v3ry_c00l_th0ugh}' > /home/ctfuser/flag.txt && chown ctfuser:ctfuser /home/ctfuser/flag.txt") | crontab -

# Expose the SSH port
EXPOSE 22

# Start the SSH service
CMD ["/usr/sbin/sshd", "-D"]
