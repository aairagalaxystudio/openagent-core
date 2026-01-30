from openagent.core.state import AgentState
from openagent.llms.base import BaseLLM


class PlannerAgent:
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def plan(self, state: AgentState) -> AgentState:
        prompt = f"""
You are a planning agent.
Break the following goal into clear, executable steps.
Return a numbered list only.

Goal:
{state.goal}
"""
        response = self.llm.generate(prompt)
        steps = [
            line.strip()
            for line in response.splitlines()
            if line.strip() and line[0].isdigit()
        ]

        state.plan = steps
        return state
