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


def prime_factors(n: int) -> list[tuple[int, int]]:
    primes = primes_to(int(math.sqrt(n) + 1))
    p_factors = []
    for prime in primes:
        if not n % prime:
            count = 0
            while not n % prime:
                count += 1
                n //= prime
            p_factors.append((prime, count))

    return p_factors
