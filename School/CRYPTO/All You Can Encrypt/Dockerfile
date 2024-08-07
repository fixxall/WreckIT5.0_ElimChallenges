FROM python:3.10-slim-buster

WORKDIR /opt

COPY ./src .

RUN apt-get update
RUN apt-get install -y nano socat
RUN pip install pycryptodome

CMD socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python -u ./chall.py'


