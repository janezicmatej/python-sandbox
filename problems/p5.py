# Problem number 5.
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
#
# What is the smallest positive number that is <dfn title="divisible with no
# remainder">evenly divisible</dfn> by all of the numbers from 1 to 20?
from fwk.problem import Problem
from utils.primes import prime_factors
from collections import defaultdict
from math import prod


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        max_prime_factors: dict[int, int] = defaultdict(int)
        for i in range(2, 21):
            for prime_factor, power in prime_factors(i).items():
                if max_prime_factors[prime_factor] < power:
                    max_prime_factors[prime_factor] = power

        return prod([prime**power for prime, power in max_prime_factors.items()])
