# Start with the base PHP image
FROM php:8.1-apache

# Install required packages
RUN apt-get update && apt-get install -y \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install PHP MySQL extensions
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Copy application source code
COPY /src /var/www/html

# Add the flag file
RUN echo "WRECKIT50{WOTABLINDTIMEBASED_PLUS_WOTABLINDCOMMANDINJECTION_UHUY}" > /flag.txt && chmod 444 /flag.txt

# Expose port 80
EXPOSE 80

ENTRYPOINT service apache2 start && /bin/bash



