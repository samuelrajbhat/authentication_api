from pydantic import BaseModel


class UserClass(BaseModel):
    username: str
    full_name: str
    email: str
    contact_number:int
    is_active: bool

class UserInDB(UserClass):
    hashed_password: str

class Access_token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username : str or None = None # type: ignore