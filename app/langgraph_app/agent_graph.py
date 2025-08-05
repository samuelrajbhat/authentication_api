from langgraph.graph import StateGraph, END, add_messages
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Literal
from langgraph.prebuilt import ToolNode, create_react_agent
from .tool_wrapper import tools
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.runtime import Runtime

llm = ChatOpenAI(model="gpt-4")
 

class State(TypedDict):
    messages: Annotated[list, add_messages]
    token: str

class Context(TypedDict):
    token: str

# agent_model = create_react_agent( model="openai:gpt-4", tools=[tools],context_schema=Context)

def agent(state: State, runtime: Runtime[Context]):
    """Agent that processes messages and invokes tools if needed."""
    messages = state["messages"]
    token = state["token"]
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

graph = graph_builder.compile()

def run_graph(user_input: str, token: str):
    result = graph.invoke({
        "messages": [
            HumanMessage(content=user_input)],
        "token": token
    }, context={"token": token})
    last_ai_message = result["messages"][-1].content
    return last_ai_message

