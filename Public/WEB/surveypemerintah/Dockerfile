# Dockerfile
FROM alpine:latest

RUN apk add --no-cache mysql-client bash curl

COPY ./insertdata.sh /insertdata.sh

RUN chmod +x /insertdata.sh

CMD ["/insertdata.sh"]
