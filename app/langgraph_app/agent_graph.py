from langgraph.graph import StateGraph, END, add_messages
from langchain_openai import ChatOpenAI
from typing import Literal
from langgraph.prebuilt import ToolNode
from .tool_wrapper import tools
from langchain_core.messages import HumanMessage, SystemMessage

from .agent_models import Context, State
from langgraph.checkpoint.memory import InMemorySaver
from .psql_memory_saver import checkpointer

# from core.config import langgraph_settings
# from langgraph.checkpoint.postgres import PostgresSaver

# LANGGRAPH_DB_URL = langgraph_settings.LANGGRAPH_DB_URL


llm = ChatOpenAI(model="gpt-4")

# checkpointer = InMemorySaver()
 


def agent(state: State):
    """Agent that processes messages and invokes tools if needed."""
    messages = state["messages"]
    llm_with_tools = llm.bind_tools(tools)
    response = llm_with_tools.invoke(messages)
    # response = agent_model.invoke(messages, context={"token": token})
    return {'messages': [response]}

tool_node = ToolNode(tools)

def should_continue(state)-> Literal["tools", END]:  # type: ignore
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END
graph_builder = StateGraph(state_schema=State, context_schema= Context)

graph_builder.add_node("agent", agent)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("should_continue", should_continue)
graph_builder.set_entry_point("agent")
graph_builder.add_conditional_edges("agent", should_continue)
graph_builder.add_edge("tools", "agent")


graph = graph_builder.compile(checkpointer=checkpointer)

def run_graph(user_input: str, token: str):
    result = graph.invoke({
        "messages": [
            HumanMessage(content=user_input)],
        "token": token},
        {"configurable": {"thread_id": "1"}}, # type: ignore
        context={"token": token})
    last_ai_message = result["messages"][-1].content
    return last_ai_message

