from fastapi import APIRouter, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from models.token_model import Token
from auth.auth_model import UserForm
from auth.password_hashing import authenticate_user, add_new_user
from auth.utils.jwt_decode import create_access_token
# from schemas.user_schemas import UserClass
from db.database import get_db
from sqlalchemy.orm import Session
from typing import Annotated



router = APIRouter()

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    print(f"Db session {db}")
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect username or password",
                            headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes=15)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/signup")
async def signup(formdata: Annotated[UserForm, Depends(UserForm.as_form)], db: Session = Depends(get_db)):
# async def signup(formdata: UserForm, db: Session = Depends(get_db)):

    print("jnskfsdf>>>>>>>>>>>>>>>>>>>>",formdata)
    add_new_user(db,formdata)
    