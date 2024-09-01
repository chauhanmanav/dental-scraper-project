import os
import config
import config.settings
from dotenv import load_dotenv 

load_dotenv()

def get_auth_token():
    return config.settings.STATIC_TOKEN

def get_base_url():
    return config.settings.BASE_URL

def get_host():
    return os.getenv("HOST") or "127.0.0.1"

def get_port():
    return os.getenv("PORT") or 8000
