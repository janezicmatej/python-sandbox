from abc import ABC, abstractmethod
from typing import Any, TypedDict, Callable, TypeVar, cast, ParamSpec, Generic
import time


class Solution(TypedDict):
    result: int
    time: float


F = TypeVar("F", bound=Callable[..., Any])
P = ParamSpec("P")
T = TypeVar("T")


def timer(fun: F) -> Callable[[F], Solution]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Solution:
        start_time = time.time()
        rtr = fun(*args, **kwargs)
        return {"result": rtr, "time": time.time() - start_time}

    return cast(F, wrapper)


class Problem(ABC):
    @classmethod
    @abstractmethod
    def solution(cls) -> int:
        pass

    @classmethod
    @timer
    def solve(cls) -> int:
        return cls.solution()


class Input(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def parse_line(cls, line: str) -> T:
        pass

    @classmethod
    def parse_input(cls, problem_number: int) -> list[T]:
        lines = []
        with open(f"inputs/p{problem_number}.txt", "r") as read_input:
            for line in read_input:
                lines.append(cls.parse_line(line))

        return lines
