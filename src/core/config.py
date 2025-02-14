import os

from dotenv import find_dotenv
from dotenv import load_dotenv
from pydantic import BaseSettings, Field

dotenv_file = find_dotenv()

load_dotenv(dotenv_path=dotenv_file)

class Settings(BaseSettings):
    PROJECT_DESCRIPTION: str = Field(
        "Default Value If PROJECT_DESCRIPTION is not set in .env",
        description="Description of the variable for context"
    )
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str= "postgres"
    POSTGRES_SERVER: str= "postgres"
    POSTGRES_PORT: int= Field(5432)
    POSTGRES_DB: str= "postgres"

    SECRET_KEY: str = "secret_for_signing_jwt"
    ALGORITHM: str= "HS256"
    TOKEN_EXPIRE_MINUTES: int = Field(30)


settings = Settings()
DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
