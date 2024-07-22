# Dockerfile
FROM alpine:latest

RUN apk add --no-cache mysql-client bash curl

COPY ./insertdata.sh /insertdata.sh

RUN chmod +x /wait-for-it.sh /insertdata.sh

CMD ["/insertdata.sh"]
