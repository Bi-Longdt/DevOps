#!/bin/bash

# Assuming your Flask app is in a directory named 'app'
APP_DIR="Desktop/Linux/DevOps"


# Update the code from your version control system (e.g., git)
cd ${APP_DIR}
git pull origin main

# Install or update dependencies
pip install -r requirements.txt

# Perform database migrations (if applicable)
# flask db upgrade

# Restart your Flask application
# gunicorn -b 0.0.0.0:5000 wsgi:app -D

# Additional deployment steps...

# Check if the deployment was successful
if [ $? -eq 0 ]; then
    echo "Deployment completed successfully."
else
    echo "Error: Deployment failed."
fi
