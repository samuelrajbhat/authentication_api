from jose import jwt, JWTError
from datetime import timedelta
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data: dict, expires_delta: timedelta or None = None): #type: ignore
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM) # type: ignore
    return encoded_jwt

def verify_token(token: str):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM) # type: ignore
        return payload
    except JWTError:
        return None