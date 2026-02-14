# Configuration settings for the Thanatos framework

class Config:
    DEBUG = True  # Enable/disable debugging
    DATABASE_URI = 'sqlite:///thanatos.db'  # Database connection string
    SECRET_KEY = 'your_secret_key_here'  # Secret key for sessions

# Utility functions

def get_database_connection():
    import sqlite3
    return sqlite3.connect(Config.DATABASE_URI)

# Additional utility functions can be added here