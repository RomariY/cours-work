import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# MEDIA
MEDIA_ROOT = 'media'
MEDIA_URL = f'{BASE_DIR}/media/'

# DATABASE
DATABASE = os.environ.get("DATABASE")
PORT = os.environ.get("DATABASE", 5432)
HOST = os.environ.get("HOST", "localhost")
DATABASE_USER = os.environ.get("DATABASE_USER")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")

