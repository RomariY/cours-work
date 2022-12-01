import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

# MEDIA
MEDIA_ROOT = 'media'
MEDIA_URL = f'{BASE_DIR}/media/'

# DATABASE
# DATABASE = os.getenv("DATABASE")
# PORT = os.getenv("PORT", 5432)
# HOST = os.getenv("HOST", "localhost")
# DATABASE_USER = os.getenv("DATABASE_USER")
# DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")

DATABASE = os.environ.get("DATABASE")
PORT = os.environ.get("PORT", 5432)
HOST = os.environ.get("HOST", "localhost")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")