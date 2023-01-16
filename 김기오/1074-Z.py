import sys

N, col, row = map(int, sys.stdin.readline().split())


def zz(n: int, r: int, c: int, acc: int):
    if n == 1:
        if (c, r) == (0, 0):
            return acc
        elif (c, r) == (0, 1):
            return acc + 1
        elif (c, r) == (1, 0):
            return acc + 2
        else:
            return acc + 3

    center = 2**(n - 1)
    mass = center ** 2
    if r < center and c < center:
        return zz(n - 1, r, c, acc)
    elif r >= center > c:
        return zz(n - 1, r - center, c, acc + mass)
    elif r < center <= c:
        return zz(n - 1, r, c - center, acc + mass * 2)
    else:
        return zz(n - 1, r - center, c - center, acc + mass * 3)


print(zz(N, row, col, 0))
