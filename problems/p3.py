# Problem number 3.
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
from fwk.solution import Problem
from utils.primes import prime_factors


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        return max(prime_factors(600851475143))
