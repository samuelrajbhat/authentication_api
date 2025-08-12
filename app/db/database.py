from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from core.config import langgraph_settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
LANGGRAPH_DB_URL = langgraph_settings.LANGGRAPH_DB_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
langgraph_engine = create_engine(LANGGRAPH_DB_URL)

SessionLocal = sessionmaker(bind=engine)
SessionLocal2 = sessionmaker(bind=langgraph_engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    
    # except Exception as e:
    #     print (f"Database connection error {e}")
    finally: 
        db.close()



