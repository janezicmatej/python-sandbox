from timeit import default_timer
from abc import ABC, abstractmethod
from typing import Any


class Problem(ABC):
    @classmethod
    @abstractmethod
    def solution(cls) -> Any:
        pass

    @classmethod
    def solve(cls) -> dict[str, int | float]:
        t_start = default_timer()
        result = cls.solution()
        timed = default_timer() - t_start
        return {"result": result, "time": timed}


class Input(ABC):
    @classmethod
    @abstractmethod
    def parse_input(cls) -> Any:
        pass
