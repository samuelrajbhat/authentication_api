from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
print("Database URL>", SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# c = engine.connect()
# try:
#     c.execute(text("SELECT * FROM users"))
#     c.close()
# except exc.DBAPIError as e:
#     if  e.connection_invalidated: 
#         print ('Cnnection was invalidated!')

# c = engine.connect()
# c.execute(text("SELECT * FROM users"))

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    
    # except Exception as e:
    #     print (f"Database connection error {e}")
    finally: 
        db.close()



