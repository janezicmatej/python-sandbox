class Problem:

    REQUIRES_INPUT: bool = False

    @classmethod
    def requires_input(cls) -> bool:
        return cls.REQUIRES_INPUT
