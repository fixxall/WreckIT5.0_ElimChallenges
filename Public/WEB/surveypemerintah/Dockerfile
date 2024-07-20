# Dockerfile
FROM alpine:latest

RUN apk add --no-cache mysql-client bash curl

COPY ./wait-for-it.sh /wait-for-it.sh
COPY ./insertdata.sh /insertdata.sh

RUN chmod +x /wait-for-it.sh /insertdata.sh

CMD ["/insertdata.sh"]
