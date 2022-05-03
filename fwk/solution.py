from abc import ABC, abstractmethod
from typing import Any, TypedDict, Callable, TypeVar, cast, ParamSpec
import time


class Solution(TypedDict):
    result: int
    time: float


F = TypeVar("F", bound=Callable[..., Any])
P = ParamSpec("P")


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


class Input(ABC):
    @classmethod
    @abstractmethod
    def parse_input(cls) -> Any:
        pass
