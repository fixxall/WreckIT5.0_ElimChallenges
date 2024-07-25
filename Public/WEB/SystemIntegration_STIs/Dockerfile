FROM python:3.10-slim-buster

RUN apt-get update && apt-get install -y nano default-mysql-client curl

WORKDIR /opt
COPY ./src .
COPY .env /opt/.env

RUN pip install --no-cache-dir -r requirements.txt

RUN curl -sSL https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh -o /wait-for-it.sh && \
    chmod +x /wait-for-it.sh

ARG FLAG
RUN echo $FLAG > flag && chmod 444 flag

COPY ./main.sh /main.sh

RUN chmod +x /main.sh

CMD ["/main.sh"]

CMD ["python", "./app.py"]
