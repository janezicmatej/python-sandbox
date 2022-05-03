import math


def primes_to(n: int) -> list[int]:
    """Input n>=6, Returns a list of primes, 2 <= p < n"""
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(n**0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3 :: 2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3 :: 2 * k] = [False] * (
                (n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1
            )
    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]


def is_prime(n: int) -> bool:
    return primes_to(n)[-1] == n


def prime_factors(n: int) -> dict[int, int]:
    primes = [2, 3, 5]
    if n >= 5:
        primes = primes_to(int(math.sqrt(n + 1)))
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

    if not p_factors:
        return {n: 1}
    return p_factors
