from typing import Dict, Any


class AgentResult:
    def __init__(self, output: str, success: bool):
        self.output = output
        self.success = success


class BaseAgent:
    """
    Base class for all agents.
    """

    def __init__(self, name: str):
        self.name = name

    def run(self, goal: str, context: Dict[str, Any] | None = None) -> AgentResult:
        raise NotImplementedError("Agents must implement run()")
