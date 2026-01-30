class BaseLLM:
    """
    Abstract LLM interface.
    """

    def generate(self, prompt: str) -> str:
        raise NotImplementedError
