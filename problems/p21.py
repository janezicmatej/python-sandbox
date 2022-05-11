# Problem number 21
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
# divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a
# and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and
# 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so
# d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
from fwk.solution import Problem
from collections import defaultdict
from utils.extended_math import divisors


class Main(Problem):
    @classmethod
    def solution(cls) -> int:
        divisor_sum = defaultdict(int)
        count = 0
        for i in range(1, 10001):
            if divisor_sum[i]:
                continue
            j = divisor_sum[i] = sum(divisors(i, proper=True))
            if j > 10001 or j < 1:
                continue
            if not divisor_sum[j]:
                divisor_sum[j] = sum(divisors(j, proper=True))
            if divisor_sum[j] == i and i != j:
                count += i + j

        return count
