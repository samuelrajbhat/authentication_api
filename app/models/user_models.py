from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index = True)
    username = Column(String, unique=True)
    email = Column(String, unique= True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_disabled = Column(Boolean, default=False)