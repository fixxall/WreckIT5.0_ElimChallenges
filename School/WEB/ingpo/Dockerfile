FROM php:7.4.33-apache
COPY index.php /var/www/html/
RUN echo "WRECKIT50{N1ce_IngPo_BozzzQu3_Mw3heh4a4h4eh3h4}" > /flag
RUN cp /usr/local/etc/php/php.ini-production /usr/local/etc/php/php.ini
RUN sed -i 's/;session.save_path = "\/tmp"/session.save_path = "\/tmp\/23104tu8-12ar-09uu-g5g7-84242k014g/g' /usr/local/etc/php/php.ini
RUN sed -i 's/;session.upload_progress.cleanup = On/session.upload_progress.cleanup = Off/g' /usr/local/etc/php/php.ini
RUN mkdir /tmp/23104tu8-12ar-09uu-g5g7-84242k014g
RUN chown www-data:www-data /var/www/html/index.php
USER www-data
EXPOSE 80
