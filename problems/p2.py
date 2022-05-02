# Problem number 2.
#
# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four
# million, find the sum of the even-valued terms.
from utils.problem import Problem
from utils.fibonacci import fib_generator


class Main(Problem):

    REQUIRES_INPUT = False

    @classmethod
    def solution(cls) -> int:
        s = 0
        fib = fib_generator()
        while True:
            term = next(fib)
            if term > 4e6:
                break
            s += term if term % 2 == 0 else 0
        return s