from models.todo_models import Todo


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
