#!/bin/bash

# Start SSH service
service ssh start

# Setup cron job to copy flag.txt every 30 seconds
echo "*/1 * * * * root cp /flag.txt /destination/flag.txt" > /etc/cron.d/copy-flag

# Give execution rights on the cron job
chmod 0644 /etc/cron.d/copy-flag

# Apply cron job
crontab /etc/cron.d/copy-flag

# Start cron in the foreground
cron -f
