from openagent.config import load_config
from openagent.llms.ollama import OllamaLLM
from openagent.core.planner import PlannerAgent
from openagent.core.executor import ExecutorAgent
from openagent.core.critic import CriticAgent
from openagent.core.loop import AgentLoop
from openagent.tools.registry import ToolRegistry
from openagent.tools.calculator import CalculatorTool


def main():
    config = load_config()

    llm = OllamaLLM(model=config["llm"]["model"])

    tools = ToolRegistry()
    tools.register(CalculatorTool())

    loop = AgentLoop(
        planner=PlannerAgent(llm),
        executor=ExecutorAgent(
            llm=llm,
            tools=tools,
            max_steps=config["agent"]["max_steps"],
        ),
        critic=CriticAgent(llm),
    )

    result = loop.run("Calculate 12 * 8 and explain agentic AI briefly")

    print("\n=== OPENAGENT RESULT ===")
    print("Completed:", result.completed)
    print("\nPlan:")
    for step in result.plan:
        print("-", step)

    print("\nOutput:")
    for out in result.step_results:
        print("-", out)


if __name__ == "__main__":
    main()
