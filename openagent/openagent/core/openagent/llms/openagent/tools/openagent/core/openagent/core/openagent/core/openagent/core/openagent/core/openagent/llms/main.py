from openagent.llms.mock import MockLLM
from openagent.core.planner import PlannerAgent
from openagent.core.executor import ExecutorAgent
from openagent.core.critic import CriticAgent
from openagent.core.loop import AgentLoop


if __name__ == "__main__":
    llm = MockLLM()

    loop = AgentLoop(
        planner=PlannerAgent(llm),
        executor=ExecutorAgent(llm),
        critic=CriticAgent(llm),
    )

    result = loop.run("Explain what agentic AI is")
    print("Completed:", result.completed)
    print("Steps:", result.plan)
    print("Output:", result.step_results)
