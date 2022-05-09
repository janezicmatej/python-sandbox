# Problem number 14
#
# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10
# terms. Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
from fwk.solution import Problem
from collections import defaultdict


def next_collatz(start: int) -> int:
    if start % 2 == 0:
        return start // 2
    else:
        return 3 * start + 1


class Main(Problem):
    lengths: dict[int, int] = defaultdict(int, {1: 1})

    @classmethod
    def length(cls, start: int) -> int:
        if start not in cls.lengths:
            cls.lengths[start] = 1 + cls.length(next_collatz(start))
        return cls.lengths[start]

    @classmethod
    def solution(cls) -> int:
        for i in range(1, 1000000):
            cls.length(i)

        return max(cls.lengths.items(), key=lambda x: x[0])[0]
