FROM php:7.4.33-apache
COPY index.php /var/www/html/
RUN echo "WRECKIT50{N1ce_IngPhoe_BoZZ}" > /flag
RUN cp /usr/local/etc/php/php.ini-production /usr/local/etc/php/php.ini
RUN sed -i 's/;session.save_path = "\/tmp"/session.save_path = "\/tmp\/83031eb8-41ac-11ee-b1b3-009337b0183d"/g' /usr/local/etc/php/php.ini
RUN sed -i 's/;session.upload_progress.cleanup = On/session.upload_progress.cleanup = Off/g' /usr/local/etc/php/php.ini
USER www-data
RUN mkdir /tmp/83031eb8-41ac-11ee-b1b3-009337b0183d && chown www-data:www-data /tmp/83031eb8-41ac-11ee-b1b3-009337b0183d
EXPOSE 80
