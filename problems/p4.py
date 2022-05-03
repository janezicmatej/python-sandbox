# Problem number 4.
#
# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
from fwk.solution import Problem


def is_palindrome(n: int) -> bool:
    return n == int("".join(reversed(list(str(n)))))


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        current = 0
        for i in range(100, 1000):
            for j in range(i, 1000):
                if is_palindrome(i * j):
                    current = i * j if i * j > current else current

        return current
