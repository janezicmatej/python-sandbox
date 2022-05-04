from itertools import accumulate, chain, cycle, count
from typing import Generator, Iterable, Iterator


def _wsieve() -> Iterator[int]:  # wheel-sieve, by Will Ness.    ideone.com/mqO25A

    # fmt: off
    wh11 = [2, 4, 2, 4, 6, 2, 6, 4, 2, 4, 6, 6, 2, 6, 4, 2, 6, 4, 6, 8, 4, 2, 4,
            2, 4, 8, 6, 4, 6, 2, 4, 6, 2, 6, 6, 4, 2, 4, 6, 2, 6, 4, 2, 4, 2, 10, 2, 10]
    # fmt: on
    cs = accumulate(chain([11], cycle(wh11)))  # roll the wheel from 11
    yield next(cs)  # cf. ideone.com/WFv4f,
    ps = _wsieve()  # codereview.stackexchange.com/q/92365/9064
    p = next(ps)  # 11
    psq = p**2  # 121
    d = dict(zip(accumulate(chain([0], wh11)), count(0)))  # wheel roll lookup dict
    mults: dict[int, Iterator[int]] = {}
    for c in cs:  # candidates, coprime with 210, from 11
        if c in mults:
            wheel = mults.pop(c)
        elif c < psq:
            yield c
            continue
        else:  # c==psq:  map (p*) (roll wh from p) = roll (wh*p) from (p*p)
            i = d[(p - 11) % 210]  # look up wheel roll starting point
            wheel = accumulate(
                chain([psq], cycle([p * d for d in wh11[i:] + wh11[:i]]))
            )
            next(wheel)
            p = next(ps)
            psq = p**2
        for m in wheel:  # pop, save in m, and advance
            if m not in mults:
                break
        mults[m] = wheel  # mults[143] = wheel@187


def primes() -> Iterator[int]:
    yield from [2, 3, 5, 7]
    yield from _wsieve()


def prime_factors(n: int) -> dict[int, int]:
    p_factors = {}
    divided_n = n
    for prime in primes():
        if prime**2 > n:
            break
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


from fwk.solution import timer


@timer
def is_prime(n: int) -> bool:
    p_factors = prime_factors(n)
    return len(p_factors) == 1 and 1 in p_factors.values()


@timer
def is_prime_2(n: int) -> bool:
    for p in primes():
        if p == n:
            return True
        if p > n:
            break
    return False
