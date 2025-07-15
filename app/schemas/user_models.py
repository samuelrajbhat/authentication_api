from pydantic import BaseModel


class UserClass(BaseModel):
    username: str
    full_name: str
    email: str
    contact_number:int
    is_active: bool

class userInDB(UserClass):
    hashed_password: str

class Access_token(BaseModel):
    access_token: str
    token_type: str

class Token_Data(BaseModel):
    username : str or None = None # type: ignore