from openagent.core.state import AgentState
from openagent.core.planner import PlannerAgent
from openagent.core.executor import ExecutorAgent
from openagent.core.critic import CriticAgent


class AgentLoop:
    def __init__(self, planner, executor, critic):
        self.planner = planner
        self.executor = executor
        self.critic = critic

    def run(self, goal: str) -> AgentState:
        state = AgentState(goal=goal)

        state = self.planner.plan(state)
        state = self.executor.execute(state)
        state = self.critic.review(state)

        return state
