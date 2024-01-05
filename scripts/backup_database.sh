#!/bin/bash

# Database information
DB_FILE="Desktop/Linux/DevOps/data/data.xlsx"
BACKUP_DIR="Desktop/Linux/DevOps/backup/directory"

# Timestamp for backup file
TIMESTAMP=$(date +%Y%m%d%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.xlsx"

# Perform database backup
cp "${DB_FILE}" "${BACKUP_FILE}"

# Check if the backup was successful
if [ $? -eq 0 ]; then
    echo "Database backup completed successfully. Backup file: ${BACKUP_FILE}"
else
    echo "Error: Database backup failed."
fi
