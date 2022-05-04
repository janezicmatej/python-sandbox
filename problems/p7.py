# Problem number 7.
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the
# 6th prime is 13.
#
# What is the 10 001st prime number?
from itertools import islice
from fwk.solution import Problem
from utils.primes import primes


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        return next(islice(primes(), 10001, None))
