from openagent.core.state import AgentState
from openagent.llms.base import BaseLLM
from openagent.tools.registry import ToolRegistry


class ExecutorAgent:
    def __init__(
        self,
        llm: BaseLLM,
        tools: ToolRegistry,
        max_steps: int = 5,
    ):
        self.llm = llm
        self.tools = tools
        self.max_steps = max_steps

    def execute(self, state: AgentState) -> AgentState:
        for step in state.plan[: self.max_steps]:
            prompt = f"""
You can use tools if needed.

Available tools:
{", ".join(self.tools.list())}

If a tool is needed, respond exactly like:
TOOL:<tool_name>:<input>

Otherwise, respond normally.

Step:
{step}
"""
            response = self.llm.generate(prompt).strip()

            if response.startswith("TOOL:"):
                _, tool_name, tool_input = response.split(":", 2)
                tool = self.tools.get(tool_name)
                if tool:
                    result = tool.run(tool_input)
                else:
                    result = f"Unknown tool: {tool_name}"
            else:
                result = response

            state.step_results.append(result)

        return state
