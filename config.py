import os

# MongoDB Configuration
MONGO_CONFIG = {
    "host": "localhost",
    "port": 27017,
    "database": "court_data",
    # Optional: Add authentication if needed
    # "username": "your_username",
    # "password": "your_password"
}

# MongoDB Connection URI
MONGO_URI = f"mongodb://{MONGO_CONFIG['host']}:{MONGO_CONFIG['port']}/{MONGO_CONFIG['database']}"

# -------------------------------
# Target Court URL
# -------------------------------
COURT_URL = "https://delhihighcourt.nic.in/app/get-case-type-status"

# -------------------------------
# Optional: App Settings
# -------------------------------
DEBUG = True           # Enable debug mode for development
SECRET_KEY = "secret!" # Required if you use Flask sessions