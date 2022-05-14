from typing import Iterator
import sys
from typing import Any, Callable, TypeVar, cast, ParamSpec


F = TypeVar("F", bound=Callable[..., Any])
P = ParamSpec("P")


def recursion_extender(depth: int = 1000) -> Callable[[F], Callable]:
    sys.setrecursionlimit(depth)

    def wrap(fun: F) -> Callable[[F], Callable]:
        def inner(*args: P.args, **kwargs: P.kwargs) -> Any:
            return fun(*args, **kwargs)

        return cast(F, inner)

    return wrap


@recursion_extender(100000)
def fib_generator(previous: int = 1, current: int = 0) -> Iterator[int]:
    yield previous + current
    for next_fib in fib_generator(current, previous + current):
        yield next_fib
