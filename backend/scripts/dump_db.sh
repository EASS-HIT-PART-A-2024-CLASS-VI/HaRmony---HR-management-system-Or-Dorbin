#!/bin/bash

DB_CONTAINER_NAME="harmony-db"

# username and password defined in the docker-compose file
DB_USER="harmony_user"
DB_NAME="harmony_db"

# the file created in the container
DUMP_FILE_IN_CONTAINER="/tmp/harmony_db_dump.sql"

# file that is taken outside of the container
DUMP_FILE_LOCAL="harmony_db_dump.sql"

echo "creating dump file inside the container..."

# commend that is running inside the container and creating dump file 
docker exec "$harmony-db" pg_dump -U "$DB_USER" "$DB_NAME" -f "$DUMP_FILE_IN_CONTAINER"

# taking the file from the container outside to the root 
docker cp "$harmony-db":"$DUMP_FILE_IN_CONTAINER" "$DUMP_FILE_LOCAL"

echo "created successfully: $DUMP_FILE_LOCAL"
