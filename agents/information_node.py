from langgraph.types import Command
from langchain_core.messages import AIMessage
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain.agents import create_agent
from tools.availability_tools import (
    check_availability_by_doctor,
    check_availability_by_specialization,
)

def information_node(llm_model):

    def node(state):

        system_prompt = """
        You are specialized agent to provide information related to doctors or hospital FAQs.
        Ask politely if more info needed.
        Current year is 2024.
        """

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("placeholder", "{messages}"),
        ])

        agent = create_agent(
            model=llm_model,
            tools=[check_availability_by_doctor, check_availability_by_specialization],
            prompt=prompt,
        )

        result = agent.invoke(state)

        return Command(
            update={
                "messages": state["messages"] + [
                    AIMessage(content=result["messages"][-1].content)
                ]
            },
            goto="supervisor",
        )

    return node