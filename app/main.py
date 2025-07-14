from fastapi import FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = ""
ALGORITHM= ""
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()
