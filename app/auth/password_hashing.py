from passlib.context import CryptContext
from schemas.user_schemas import UserInDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if  username in db:
        user_data = db[username]
        return UserInDB(**user_data)
    else: 
        return

def authenticate_user(db, username:str, password: str):
    user = get_user(db, username= username)
    if not  user :
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


