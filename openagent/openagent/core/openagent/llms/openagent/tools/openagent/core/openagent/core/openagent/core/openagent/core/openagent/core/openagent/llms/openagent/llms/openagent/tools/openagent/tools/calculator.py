from openagent.tools.base import Tool


class CalculatorTool(Tool):
    name = "calculator"
    description = "Evaluate basic math expressions"

    def run(self, input: str) -> str:
        try:
            return str(eval(input, {}, {}))
        except Exception as e:
            return f"Error: {e}"
