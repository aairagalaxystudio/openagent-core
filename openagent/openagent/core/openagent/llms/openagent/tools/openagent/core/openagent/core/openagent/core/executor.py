from openagent.core.state import AgentState
from openagent.llms.base import BaseLLM


class ExecutorAgent:
    def __init__(self, llm: BaseLLM, max_steps: int = 5):
        self.llm = llm
        self.max_steps = max_steps

    def execute(self, state: AgentState) -> AgentState:
        for idx, step in enumerate(state.plan[: self.max_steps]):
            prompt = f"""
Execute the following step precisely.

Step:
{step}
"""
            result = self.llm.generate(prompt)
            state.step_results.append(result)

        return state
