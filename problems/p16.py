# Problem number 16
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
from fwk.solution import Problem


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        return sum(map(int, list(str(2**1000))))
