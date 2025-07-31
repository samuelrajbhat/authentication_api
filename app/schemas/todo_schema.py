from pydantic import BaseModel
from typing import Optional

from datetime import datetime
from models.todo_models import TodoStatus


class TodoForm(BaseModel):
    
    title: str
    description: Optional[str]
    status: Optional[TodoStatus]= TodoStatus.pending

class TodoOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TodoStatus
    created_at: datetime
    updated_at: datetime

    class config:
        orm_mode = True
        use_enum_values = True


class UpdateTodoStatus(BaseModel):
    status: Optional[TodoStatus]= TodoStatus.pending
