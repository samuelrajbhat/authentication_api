from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL>", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    
    # except Exception as e:
    #     print (f"Database connection error {e}")
    finally: 
        db.close()



