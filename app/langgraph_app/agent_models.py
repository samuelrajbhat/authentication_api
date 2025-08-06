from typing import Annotated, TypedDict
from langgraph.graph import add_messages
from pydantic import BaseModel
class State(TypedDict):
    messages: Annotated[list, add_messages]
    token: str

class Context(TypedDict):
    token: str

class LLMRequest(BaseModel):
    messages: str
