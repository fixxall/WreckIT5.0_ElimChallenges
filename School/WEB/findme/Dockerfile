FROM php:7.4-apache

COPY app/php.ini /usr/local/etc/php/

COPY app/ /var/www/html/

RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html

RUN useradd -m LFI_lfi_LF1_lfI_ezpz_ye4h

RUN chown www-data:www-data /etc/passwd && chmod 644 /etc/passwd

RUN echo 'LogLevel debug' >> /etc/apache2/apache2.conf

RUN echo 'display_errors = On' >> /usr/local/etc/php/php.ini

EXPOSE 80
