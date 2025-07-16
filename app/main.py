from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# from config import settings
from db.database import engine
from models.user_models import Base


SECRET_KEY = "8TTzECHDig3XMcNMLdqco8gebhAPyq4cPws_YNxdNaE"
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

db = {
    "samuel": {
        "username": "samuel",
        "full_name": "Samuel Raj Bhat",
        "email": "samuelrajbhat5@gmail.com",
        "hashed_password": "$2b$12$KAo5UvLGtAQEQmOvDw2Vwu9qINNgKaWQAp9eUyXmJs6MSSoxNnju6",
        "disabled": False
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None # type: ignore

class User(BaseModel):
    username: str
    email :str
    full_name: str
    disabled: bool

class UserInDB(User):
    hashed_password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")
oauth_2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def verify_password(plain_passoword, hashed_password):
    return pwd_context.verify(plain_passoword, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data)
    else:
        return

def authenticate_user(db, username: str, password: str):
    user = get_user(db, username)
    if not user: 
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta or None= None): #type: ignore
    to_encode= data.copy()
    
    if expires_delta: 
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth_2_scheme)):
    credential_exception = HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub") # type: ignore
        if username is None:
            raise credential_exception
        token_data = TokenData(username= username)


    except JWTError:
         raise credential_exception
    
    user = get_user(db, username= token_data.username) # type: ignore

    if user is None:
        raise credential_exception
    return user


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail="Inactive User" )
    
    return current_user

app = FastAPI()

Base.metadata.create_all(bind = engine)


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password) #type: ignore
    if  not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail={"Incorrect username or password"},
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data= {"sub": user.username}, expires_delta= access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


user_password = "pasword123"
hash_password = get_password_hash(user_password)
print(">>>>>>>",hash_password)