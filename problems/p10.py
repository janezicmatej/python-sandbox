# Problem number 10
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
from fwk.solution import Problem
from utils.primes import primes


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        prime_sum = 0
        for prime in primes():
            if prime > 2000000:
                break
            prime_sum += prime

        return prime_sum
