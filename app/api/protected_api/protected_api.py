from fastapi import APIRouter, Depends, Security
from dependencies.auth_user import get_current_active_user
from schemas.todo_schema import TodoForm, UpdateTodoStatus, TodoOut
from sqlalchemy.orm import Session
from db.database import get_db
from services.todo_services import list_all_todo, add_new_todo, upadte_todo_status, delete_todo_with_id
from models.user_models import Users
from typing import List



protected_router = APIRouter(prefix="/secure",
                   dependencies=[Security(get_current_active_user)])

@protected_router.get("/protected")
def protected_route(current_user: dict = Depends(get_current_active_user)):
    return {"message": "welcome to the protected route!", "user": current_user} # type: ignore

@protected_router.post("/todos")
def todos(todo_data: TodoForm, db: Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    todo= add_new_todo(todo_data, db, current_user)
    return {"added":f"{todo}"}

@protected_router.patch("/todos")
def update(todo_id: int,
           update_status:UpdateTodoStatus,
           db: Session= Depends(get_db),
            current_user: Users= Depends(get_current_active_user)):
    todo_updated = upadte_todo_status(todo_id, update_status, db, current_user)
    return todo_updated

@protected_router.get("/todos", response_model= List[TodoOut])
def get(db: Session = Depends(get_db), current_user: Users = Depends(get_current_active_user)):
    todo_list= list_all_todo(db, current_user)
    return todo_list

@protected_router.delete("/delete")
def delete( todo_id: int, db:Session = Depends(get_db),current_user: Users = Depends(get_current_active_user)):
    todo_delete = delete_todo_with_id(todo_id, db, current_user)
    return todo_delete