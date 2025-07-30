from fastapi import APIRouter, Depends, Security
from dependencies.auth_user import get_current_active_user



protected_router = APIRouter(prefix="/secure",
                   dependencies=[Security(get_current_active_user)])

@protected_router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_active_user)):
    return {"message": "welcome to the protected route!", "user": current_user} # type: ignore

@protected_router.post("/add_item")
def add_item():
    return {"message": "This is protected route"}