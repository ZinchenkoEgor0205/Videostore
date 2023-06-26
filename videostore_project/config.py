import os

from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.environ.get("NAME")
DB_HOST = os.environ.get("HOST")
DB_PORT = os.environ.get("PORT")
DB_USER = os.environ.get("USER")
DB_PASS = os.environ.get("PASSWORD")
