from langgraph.types import Command
from langchain_core.messages import AIMessage
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain.agents import create_agent
from tools.cancel_appointment import cancel_appointment
from tools.set_appointment import set_appointment
from tools.reschuduler_appointment import reschedule_appointment

def booking_node(llm_model):

    def node(state):

        system_prompt = """
        You are specialized agent to set, cancel or reschedule appointment.
        Ask politely if more info needed.
        Current year is 2024.
        """

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("placeholder", "{messages}"),
        ])

        agent = create_agent(
            model=llm_model,
            tools=[set_appointment, cancel_appointment, reschedule_appointment],
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