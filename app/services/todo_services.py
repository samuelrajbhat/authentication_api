from fastapi import status, HTTPException
from models.todo_models import Todo
from fastapi.responses import JSONResponse

def list_all_todo(db, current_user):
    todos = db.query(Todo).filter(Todo.owner_id == current_user.id).all()
    return todos if todos is not None else []


def add_new_todo(todo_data, db, current_user):
    todo = Todo(
        title = todo_data.title,
        description = todo_data.description,
        status = todo_data.status,
        owner_id = current_user.id
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def upadte_todo_status(todo_id,update_status, db, current_user):
    
    todo_to_update = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == current_user.id).first()
    if not todo_to_update:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = "Todo Not found")

    todo_to_update.status = update_status.status
    db.commit()
    db.refresh(todo_to_update)
    return {"updated_status": todo_to_update.status}

def delete_todo_with_id(todo_id, db, current_user):
    todo_item = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == current_user.id).first()

    if not todo_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    db.delete(todo_item)
    db.commit()
    return {"message": "Deletion compatiblel"}