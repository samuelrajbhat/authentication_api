from pydantic import BaseModel


class UserClass(BaseModel):
    id: int
    username: str
    full_name: str
    email: str
    is_disabled: bool
    model_config = {
        "from_attributes": True 
        # To allow instantiating this pydantic model from SQLAlchemy objects (or any other  attributes) using model_validate()

    }

class UserInDB(UserClass):
    hashed_password: str
    model_config = {
        "from_attributes": True 
        # To allow instantiating this pydantic model from SQLAlchemy objects (or any other  attributes) using model_validate()

    }

class Access_token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username : str or None = None # type: ignore