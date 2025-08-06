from typing import Annotated, TypedDict
from langgraph.graph import add_messages

class State(TypedDict):
    messages: Annotated[list, add_messages]
    token: str

class Context(TypedDict):
    token: str
