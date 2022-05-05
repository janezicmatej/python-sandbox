from typing import Iterator

from .primes import prime_factors
import math
import itertools


def pythagorean_triplets(limit: int) -> list[tuple[int, int, int]]:
    triplets = []
    c = 0
    m = 2
    while c < limit:
        for n in range(1, m + 1):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            if c > limit:
                break
            if a == 0 or b == 0 or c == 0:
                break
            triplets.append((a, b, c))
        m += 1

    return triplets


def factors(n: int, sort: bool = False) -> list[int]:
    p_factors = prime_factors(n)
    listed = []
    for k, v in p_factors.items():
        listed += [k] * v
    s: set[tuple[int, ...]] = {(1,)}

    for i in range(1, sum(p_factors.values()) + 1):
        for comb in itertools.combinations(listed, i):
            s.add(comb)

    prod_combs = [math.prod(comb) for comb in s]
    if sort:
        return sorted(prod_combs)
    return prod_combs


def natural_numbers(start: int = 1) -> Iterator[int]:
    while True:
        yield start
        start += 1
