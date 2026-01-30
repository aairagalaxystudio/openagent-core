from openagent.core.state import AgentState
from openagent.llms.base import BaseLLM


class CriticAgent:
    def __init__(self, llm: BaseLLM):
        self.llm = llm

    def review(self, state: AgentState) -> AgentState:
        combined_output = "\n".join(state.step_results)

        prompt = f"""
You are a critic agent.
Decide if the goal has been successfully completed.

Goal:
{state.goal}

Result:
{combined_output}

Answer ONLY YES or NO.
"""
        verdict = self.llm.generate(prompt).strip().upper()
        state.completed = verdict.startswith("YES")
        return state
