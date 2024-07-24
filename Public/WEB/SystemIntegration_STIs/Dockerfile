FROM python:3.10.6-slim-buster

RUN apt-get update
RUN apt-get install -y nano socat
# RUN apt-get install -y 
RUN pip install -r requirements.txt

WORKDIR /opt
COPY ./src .

CMD socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python -u ./app.py'