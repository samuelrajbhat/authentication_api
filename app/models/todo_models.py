
from sqlalchemy import Integer, Column, String, Text, Boolean, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
import enum
from db.database import Base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from models.user_models import Users


class TodoStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int]= mapped_column(Integer, primary_key=True, index= True)
    title = Column(String(100), nullable = False)
    description = Column(Text, nullable = True)
    status = Column(Enum(TodoStatus), default=TodoStatus.pending)

    created_at = Column(DateTime, default = datetime.now)
    updated_at = Column(DateTime, default= datetime.now, onupdate=datetime.now)

    # Foreign Key to link to the user
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    owner: Mapped["Users"] = relationship(back_populates="todos")
