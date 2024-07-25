#!/bin/bash

# Load environment variables from .env file
set -a
. /opt/.env
set +a

DB_HOST=$(echo "$DB_HOST" | tr -d '\r\n')
DB_USER=$(echo "$DB_USER" | tr -d '\r\n')
DB_PASSWORD=$(echo "$DB_PASSWORD" | tr -d '\r\n')
DB_DATABASE=$(echo "$DB_DATABASE" | tr -d '\r\n')
SEED=$(echo "$SEED" | tr -d '\r\n')

/wait-for-it.sh "$DB_HOST":3306 -- echo "MySQL is up - initializing database"

>&2 echo "MySQL is up - initialization"

mysql -h"$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" "$DB_DATABASE" -e "INSERT INTO users (username, password) VALUES ('admin', '$SEED'), ('user', 'user');"

exec python -u /opt/app.py