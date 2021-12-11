import secrets
from pydantic import BaseSettings
from decouple import config

class Settings(BaseSettings):

    # General FastAPI
    PROJECT_NAME: str = 'leonardodepaula.com'
    PROJECT_VERSION: str = '1.0.0'
    SECRET_KEY: str = secrets.token_urlsafe(32)

    # Database
    POSTGRES_USER : str = config('POSTGRES_USER')
    POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
    POSTGRES_SERVER : str = config('POSTGRES_SERVER', 'localhost')
    POSTGRES_PORT : str = config('POSTGRES_PORT', 5432)
    POSTGRES_DB : str = config('POSTGRES_DB')
    DATABASE_URL = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}'

settings = Settings()