from langgraph.types import Command
from langgraph.graph import END
from langchain_core.messages import HumanMessage
from prompts.prompt import system_prompt
from agents.state import Router, AgentState

def supervisor_node(llm_model):

    def node(state: AgentState):

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"user's identification number is {state['id_number']}"},
        ] + state["messages"]

        response = llm_model.with_structured_output(Router).invoke(messages)

        goto = response["next"]

        if goto == "FINISH":
            goto = END

        return Command(
            goto=goto,
            update={
                "next": goto,
                "current_reasoning": response["reasoning"],
            },
        )

    return node