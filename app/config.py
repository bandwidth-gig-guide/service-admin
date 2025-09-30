import os

DB_HOST = os.getenv('DB_HOST', 'invalid')
DB_PORT = os.getenv('DB_PORT', 'invalid')
DB_USER = os.getenv('DB_USER', 'invalid')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'invalid')
DB_NAME = os.getenv('DB_NAME', 'invalid')
DB_SSL_MODE = os.getenv('DB_SSL_MODE', "require") # Use "disable" for local dev.
