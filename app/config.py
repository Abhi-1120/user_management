import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings


__all__ = ['Config']

load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env')))


class Config(BaseSettings):
    DEBUG: int = 0
    PORT: int = int(os.environ.get('PORT', '5000'))
    MYSQL_DATABASE_HOST: str = os.environ.get("MYSQL_DATABASE_HOST")
    MYSQL_DATABASE: str = os.environ.get("MYSQL_DATABASE")
    MYSQL_DATABASE_USER: str = os.environ.get("MYSQL_DATABASE_USER")
    MYSQL_DATABASE_PASSWORD: str = os.environ.get("MYSQL_DATABASE_PASSWORD")
    MYSQL_DATABASE_PORT: int = os.environ.get("MYSQL_DATABASE_PORT")
