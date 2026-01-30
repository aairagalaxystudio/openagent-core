class Tool:
    name: str
    description: str

    def run(self, input: str) -> str:
        raise NotImplementedError
