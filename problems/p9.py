# Problem number 9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#  a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find the
# product abc.
from fwk.solution import Problem
from utils.extended_math import pythagorean_triplets


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        result = 0
        for a, b, c in pythagorean_triplets(1000):
            if a + b + c == 1000:
                result = a * b * c
                break

        return result
