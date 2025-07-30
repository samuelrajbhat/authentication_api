from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import List, TYPE_CHECKING

from db.database import Base

if TYPE_CHECKING:
    from models.todo_models import Todo



class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index = True)
    username = Column(String, unique=True)
    email = Column(String, unique= True)
    full_name = Column(String)
    hashed_password = Column(String)
    is_disabled = Column(Boolean, default=False)
    
    todos: Mapped[List["Todo"]] = relationship("Todo",back_populates="owner")

 