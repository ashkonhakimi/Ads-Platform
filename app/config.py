import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development") # default = dev environment

APP_HOST = os.getenv("APP_HOST", "0.0.0.0") # defaults for dev
APP_PORT = int(os.getenv("APP_PORT", 8000)) # defaults for dev

DEBUG = APP_ENV == "development"

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ads.db") # default if not found