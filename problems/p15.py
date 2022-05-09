# Problem number 15
#
# Starting in the top left corner of a 2×2 grid, and only being able to move to the
# right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?
from fwk.solution import Problem
import math


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        return math.comb(40, 20)
