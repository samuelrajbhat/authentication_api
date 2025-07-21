import os
from dotenv import load_dotenv

from pathlib import Path
env__path = Path(".")/".env"
load_dotenv(dotenv_path=env__path)

class Settings:
    PROJECT_NAME: str = "Auth App"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str | None = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str | None = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER:str = os.getenv("POSTGRES_SERVER", "postgres")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB : str | None = os.getenv("POSTGRES_DB", "postres")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY : str = os.getenv("SECRET_KEY", "")
    ALGORITHM : str | None = os.getenv("ALGORITHM")

settings = Settings()