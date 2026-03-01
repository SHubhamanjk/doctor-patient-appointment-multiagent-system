from langgraph.graph import StateGraph, START
from agents.state import AgentState
from agents.supervisor import supervisor_node
from agents.information_node import information_node
from agents.booking_node import booking_node

def build_graph(llm_model):

    graph = StateGraph(AgentState)

    graph.add_node("supervisor", supervisor_node(llm_model))
    graph.add_node("information_node", information_node(llm_model))
    graph.add_node("booking_node", booking_node(llm_model))

    graph.add_edge(START, "supervisor")

    return graph.compile()