import os

from dotenv import find_dotenv
from dotenv import load_dotenv

dotenv_file = find_dotenv()

load_dotenv(dotenv_path=dotenv_file)
dotenv_file = find_dotenv()


class Settings:
    PROJECT_NAME: str = "Fast API"
    PROJECT_VERSION: str = "0.0.1"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv(
        "POSTGRES_PORT", 5432
    )  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    SECRET_KEY = os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    TOKEN_EXPIRE_MINUTES = os.getenv("TOKEN_EXPIRE_MINUTES")


settings = Settings()
