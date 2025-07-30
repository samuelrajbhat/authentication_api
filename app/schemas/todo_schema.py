from pydantic import BaseModel
from typing import Annotated, Optional
from fastapi import Form
from sqlalchemy import Enum
from models.todo_models import TodoStatus


class TodoForm(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: Optional[TodoStatus]= TodoStatus.pending


    # @classmethod
    # def as_form(
    #         cls,
    #         username: Annotated[str, Form()], # type: ignore
    #         full_name: Annotated[str, Form()], # type: ignore
    #         email: Annotated[str, Form()], # type: ignore
    #         password: Annotated[str, Form()], # type: ignore
    # ) -> "UserForm": # type: ignore
    #     return cls(username = username,
    #         full_name = full_name,
    #         email = email,
    #         password = password) 