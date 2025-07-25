from pydantic import BaseModel
from typing import Annotated
from fastapi import Form


class UserForm(BaseModel):
    username: str
    full_name: str
    email: str
    password: str

    @classmethod
    def as_form(
            cls,
            username: Annotated[str, Form()], # type: ignore
            full_name: Annotated[str, Form()], # type: ignore
            email: Annotated[str, Form()], # type: ignore
            password: Annotated[str, Form()], # type: ignore
    ) -> "UserForm": # type: ignore
        return cls(username = username,
            full_name = full_name,
            email = email,
            password = password) 