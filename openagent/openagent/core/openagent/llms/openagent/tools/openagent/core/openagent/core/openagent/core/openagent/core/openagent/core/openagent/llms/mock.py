from openagent.llms.base import BaseLLM


class MockLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        if "numbered list" in prompt.lower():
            return "1. Think\n2. Answer"
        if "YES or NO" in prompt:
            return "YES"
        return "This is a mock response."
