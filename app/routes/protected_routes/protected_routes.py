from fastapi import APIRouter, Depends, Security
from dependencies.auth_user import get_current_active_user

router = APIRouter()

@router.get("/protected")
def protected_router(current_user: dict = Security(get_current_active_user)):
    return {"message": "welcome to the protected route!", "user": current_user}