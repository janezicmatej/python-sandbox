from typing import Iterator


def fib_generator(previous: int = 1, current: int = 0) -> Iterator[int]:
    yield previous + current
    for next_fib in fib_generator(current, previous + current):
        yield next_fib
