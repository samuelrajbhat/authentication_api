import os
from dotenv import load_dotenv

from pathlib import Path
env__path = Path(__file__).resolve().parents[2]/".env"
load_dotenv(dotenv_path=env__path)

class Settings:
    PROJECT_NAME: str = "Auth App"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER: str | None = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str | None = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER:str = os.getenv("POSTGRES_SERVER", "postgres")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    POSTGRES_DB : str | None = os.getenv("POSTGRES_DB", "postgres")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY : str = os.getenv("SECRET_KEY", "")
    ALGORITHM : str | None = os.getenv("ALGORITHM")

settings = Settings()

class LangGraphSettings:
    LANGGRAPH_DB: str = os.getenv("LANGGRAPH_DB", "langgraph_checkpointer")
    LANGGRAPH_DB_URL: str = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{LANGGRAPH_DB}"
    
langgraph_settings= LangGraphSettings()