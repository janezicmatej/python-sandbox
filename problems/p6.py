# Problem number 6.
#
# The sum of the squares of the first ten natural numbers is,
#
# The square of the sum of the first ten natural numbers is,
#
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is $3025 - 385 = 2640$.
#
# Find the difference between the sum of the squares of the first one hundred natural
# numbers and the square of the sum.
from fwk.solution import Problem


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        return sum([x for x in range(1, 101)]) ** 2 - sum(
            [x**2 for x in range(1, 101)]
        )
