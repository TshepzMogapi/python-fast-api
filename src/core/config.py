import os

from dotenv import find_dotenv
from dotenv import load_dotenv
from pydantic import BaseSettings

dotenv_file = find_dotenv()

load_dotenv(dotenv_path=dotenv_file)

class Settings(BaseSettings):
    PROJECT_NAME: str = "Fast API"
    PROJECT_VERSION: str = "0.0.1"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: int
    POSTGRES_DB: str

    SECRET_KEY: str
    ALGORITHM: str
    TOKEN_EXPIRE_MINUTES: int


settings = Settings()
DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
