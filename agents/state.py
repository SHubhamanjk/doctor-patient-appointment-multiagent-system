from typing import Literal, Any
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages

class Router(TypedDict):
    next: Literal["information_node", "booking_node", "FINISH"]
    reasoning: str

class AgentState(TypedDict):
    messages: Annotated[list[Any], add_messages]
    id_number: int
    next: str
    query: str
    current_reasoning: str