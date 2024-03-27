import sys


def find(x: int):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(a: int, b: int):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def func():
    for i in range(N):
        num = int(sys.stdin.readline())
        parent = find(num)
        if parent == 0:
            return i
        union(parent - 1, num)

    return N


G, N = int(input()), int(input())
parents = list(range(G + 1))

print(func())
