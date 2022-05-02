from timeit import default_timer
from abc import ABC, abstractmethod
from typing import Any


class Problem(ABC):

    REQUIRES_INPUT: bool = False

    @classmethod
    def requires_input(cls) -> bool:
        return cls.REQUIRES_INPUT

    @classmethod
    @abstractmethod
    def solution(cls) -> Any:
        pass

    @classmethod
    def solve(cls, verbose: bool = False) -> None:
        t_start = default_timer()
        result = cls.solution()
        timed = default_timer() - t_start
        if verbose:
            print(f"The result [{result}] was calculated in {timed}ms time.")
        else:
            print(f"{result}, {timed}ms")
        with open("solution.txt", "w") as solution:
            solution.write(f"{result}")
