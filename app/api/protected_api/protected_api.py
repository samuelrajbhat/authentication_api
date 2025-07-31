from fastapi import APIRouter, Depends, Security
from dependencies.auth_user import get_current_active_user
from schemas.todo_schema import TodoForm
from sqlalchemy.orm import Session
from db.database import get_db
from services.todo_services import add_new_todo
from models.user_models import Users



protected_router = APIRouter(prefix="/secure",
                   dependencies=[Security(get_current_active_user)])

@protected_router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_active_user)):
    return {"message": "welcome to the protected route!", "user": current_user} # type: ignore

@protected_router.post("/todos")
def todos(todo_data: TodoForm, db: Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    todo= add_new_todo(todo_data, db, current_user)
    return {"added":f"{todo}"}