from pydantic import BaseModel
from typing import Annotated
from fastapi import Form


class UserForm(BaseModel):
    def __init__(
            self,
            username: Annotated[str, Form()], # type: ignore
            full_name: Annotated[str, Form()], # type: ignore
            email: Annotated[str, Form()], # type: ignore
            password: Annotated[str, Form()], # type: ignore
    ):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.password = password
        