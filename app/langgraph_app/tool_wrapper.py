from langchain_core.tools import tool

from .crud_function import add_todo, get_todos

@tool
def fetch_todos(token: str) -> str:
    """fetch all todos form the  user"""
    todos = get_todos(unclean_token=token)
    return str(todos)

@tool
def create_todos(token:str, title: str, description: str, status: str):
    """Create new todo for  the user"""
    new_todos = add_todo(unclean_token=token, title=title, description=description, status=status)
    return new_todos

tools = [fetch_todos, create_todos]
