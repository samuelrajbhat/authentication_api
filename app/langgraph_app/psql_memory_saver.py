from langgraph.checkpoint.postgres import PostgresSaver
from core.config import langgraph_settings
from langgraph.graph import MessagesState

from langchain_core.runnables import RunnableConfig
from langgraph.store.base import BaseStore

DATABASE_URL = langgraph_settings.LANGGRAPH_DB_URL

checkpointer_ctx = PostgresSaver.from_conn_string(DATABASE_URL)

checkpointer = checkpointer_ctx.__enter__()