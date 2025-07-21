from fastapi import FastAPI
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from pydantic import BaseModel
# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext

from core.config import settings
from db.database import engine
from models.user_models import Base



from routes.auth_routes import router as auth_router 

app = FastAPI()

Base.metadata.create_all(bind = engine)
print("conneccting to dattabase", settings.DATABASE_URL)


app.include_router(auth_router)


# @app.post("/token", response_model=Token)
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(db, form_data.username, form_data.password) #type: ignore
#     if  not user:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#                             detail={"Incorrect username or password"},
#                             headers={"WWW-Authenticate": "Bearer"})
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(data= {"sub": user.username}, expires_delta= access_token_expires)
#     return {"access_token": access_token, "token_type": "bearer"}

# @app.get("/users/me", response_model=User)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     return current_user


