import math


def primes_to(n: int) -> list[int]:
    # naive implementation of prime sieve, should be looked at in the future
    s = set(range(2, n + 1))
    primes = set()
    while s:
        prime = s.pop()
        primes.add(prime)
        s.difference_update({prime * i for i in range(1, int((n + 1) / prime + 1))})

    return list(primes)


def is_prime(n: int) -> bool:
    return primes_to(n)[-1] == n


def prime_factors(n: int) -> dict[int, int]:
    primes = primes_to(n)
    if primes[-1] == n:
        return {n: 1}
    p_factors = {}
    divided_n = n
    for prime in primes:
        if divided_n == 1 or prime**2 > n:
            break
        if not divided_n % prime:
            count = 0
            while not divided_n % prime:
                count += 1
                divided_n //= prime
            p_factors[prime] = count

    return p_factors
