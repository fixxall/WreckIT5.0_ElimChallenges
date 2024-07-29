FROM ubuntu:latest

# Create a flag file
RUN echo "CTF{docker_escape_success}" > /flag.txt

# Run as a non-privileged user
RUN useradd -ms /bin/bash flaguser
USER flaguser

CMD ["tail", "-f", "/dev/null"]
