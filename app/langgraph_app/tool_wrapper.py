from langchain_core.tools import tool
from langgraph.runtime import get_runtime
# from langgraph_app.agent_graph import Context

from .crud_function import add_todo, get_todos, update_todo_status, delete_todo_item
@tool
def fetch_todos() -> str:
    """fetch all todos form the  user"""
    runtime = get_runtime(Context)
    # token_ = runtime.context.token
    todos = get_todos( runtime.context.token) # type: ignore
    return str(todos)

@tool
def create_todos(token:str, title: str, description: str, status: str):
    """Create new todo for  the user"""
    new_todos = add_todo(unclean_token=token, title=title, description=description, status=status)
    return new_todos

@tool
def update_todo(token: str, new_status: str, todo_id: int):
    """Update the status of a todo with given todo_id."""
    updated_todo = update_todo_status(token=token, new_status=new_status, todo_id = todo_id)
    return  updated_todo

@tool
def delete_todo(token: str, todo_id: int):
    """Delete a todo item with the given todo_id."""
    deleted_todo = delete_todo_item(token= token, todo_id= todo_id)
    return deleted_todo

tools = [fetch_todos, create_todos, update_todo, delete_todo]
