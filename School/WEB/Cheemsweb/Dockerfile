# Base image
FROM php:7.4-apache

# Copy application files
COPY app/ /var/www/html/
COPY admin/ /var/www/html/admin/
COPY app/img/ /var/www/html/img/

# Set permissions
RUN chown -R www-data:www-data /var/www/html/ && chmod -R 755 /var/www/html/

# Restrict access to the admin directory
RUN echo "<Directory /var/www/html/admin>\n\
    Require local\n\
</Directory>" > /etc/apache2/conf-available/admin.conf \
    && a2enconf admin

# Enable Apache modules and configurations
RUN a2enmod rewrite
RUN echo "AllowEncodedSlashes NoDecode" >> /etc/apache2/apache2.conf
RUN echo "php_flag display_errors on" > /etc/apache2/conf-available/php-errors.conf \
    && echo "php_value error_reporting 32767" >> /etc/apache2/conf-available/php-errors.conf \
    && a2enconf php-errors

# Create flag directory and set permissions
RUN mkdir /flag
RUN echo "WRECKIT50{server_side_rem0te_f0rgeryyyy}" > /flag/flag
RUN chmod 644 /flag/flag

# Expose port 80
EXPOSE 80

# Start Apache
CMD ["apache2-foreground"]
