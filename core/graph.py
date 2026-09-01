from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from core.llm_client import get_llm

# State definition
class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# Main node -- calling the model
def call_model(state: AgentState):
    llm = get_llm()
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

def build_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("agent", call_model)
    workflow.add_edge(START, "agent")
    workflow.add_edge("agent", END)
    
    return workflow.compile()