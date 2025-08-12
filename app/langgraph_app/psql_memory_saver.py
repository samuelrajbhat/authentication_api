from langgraph.checkpoint.postgres import PostgresSaver
from core.config import langgraph_settings
from langgraph.graph import MessagesState


from langgraph.store.base import BaseStore
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4.1-mini")


DATABASE_URL = langgraph_settings.LANGGRAPH_DB_URL


checkpointer_ctx = PostgresSaver.from_conn_string(DATABASE_URL)

checkpointer = checkpointer_ctx.__enter__()

def classify_conversation_type(message: str) -> str:
    prompt = f""" 
        You are a classifier that determines the type of conversation based on the provided message.
        Your task is to classify the conversation into one of the following categories:
        general: The user is asking a general question or seeking information.
        todo: The user is discussing a task or to-do item.
        RESPOND WITH THE CATEGORY NAME ONLY, WITHOUT ANY ADDITIONAL TEXT.
        {message}
"""
    response = llm.invoke(prompt)
    return response.content.strip().lower() # type: ignore

def get_thread_id(conversation_type: str) -> str:
    """Generate a thread ID based on the conversation type."""
    return f"{conversation_type}_thread"

def create_configurable_thread_id(message: str) -> str:
    conversation_type = classify_conversation_type(message)
    return get_thread_id(conversation_type)