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
