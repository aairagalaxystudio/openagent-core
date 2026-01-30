from typing import List, Dict, Any


class AgentState:
    def __init__(self, goal: str):
        self.goal = goal
        self.plan: List[str] = []
        self.step_results: List[str] = []
        self.completed: bool = False
        self.metadata: Dict[str, Any] = {}
