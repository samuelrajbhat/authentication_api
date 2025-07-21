from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from models.user_models import Base

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL>", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    
    # except Exception as e:
    #     print (f"Database connection error {e}")
    finally: 
        db.close()



