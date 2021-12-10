import secrets
from pydantic import BaseSettings

class Settings(BaseSettings):

    PROJECT_NAME: str = 'leonardodepaula.com'
    PROJECT_VERSION: str = '1.0.0'
    SECRET_KEY: str = secrets.token_urlsafe(32)

settings = Settings()