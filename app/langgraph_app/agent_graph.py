from langgraph.graph import StateGraph, END, add_messages
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Literal
from langgraph.prebuilt import ToolNode
from .tool_wrapper import tools
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(model="gpt-4")
 

class State(TypedDict):
    messages: Annotated[list, add_messages]
    token: str
def agent(state: State):
   messages = state["messages"]
   token = state["token"]
   llm_with_tools = llm.bind_tools(tools)
   response = llm_with_tools.invoke(messages)
   return {'messages': [response]}

tool_node = ToolNode(tools)

def should_continue(state)-> Literal["tools", END]:  # type: ignore
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return END
graph_builder = StateGraph(State)

graph_builder.add_node("agent", agent)
graph_builder.add_node("tools", tool_node)
graph_builder.add_node("should_continue", should_continue)
graph_builder.set_entry_point("agent")
graph_builder.add_conditional_edges("agent", should_continue)
graph_builder.add_edge("tools", "agent")

graph = graph_builder.compile()

def run_graph(user_input: str, token: str):
    result = graph.invoke({
        "messages": [SystemMessage(content=f"The user's tokenn is {token}. Use this when calling tools."),
            HumanMessage(content=user_input)],
        "token": token
    })
    last_ai_message = result["messages"][-1].content
    return last_ai_message

