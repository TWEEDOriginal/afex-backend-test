from .base import *
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
# Override base settings here

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": DB_NAME,
        "USER": USER_NAME,
        "PASSWORD": PASSWORD,
        "HOST": HOST,
        "PORT": DB_PORT,
    }
}
