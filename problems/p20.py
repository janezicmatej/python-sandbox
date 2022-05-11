# Problem number 20
#
# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,and the sum of the digits in the
# number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
from fwk.solution import Problem
import math


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        return sum(map(int, list(str(math.factorial(100)))))
