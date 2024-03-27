import sys
from heapq import heappop, heappush


def get_max():
    acc = 0
    values = []
    for i in range(K):
        while jewels and jewels[0][0] <= bags[i]:
            heappush(values, -heappop(jewels)[1])
        if values:
            acc -= heappop(values)
    return acc


N, K = map(int, sys.stdin.readline().split())
jewels, bags = [], []
for _ in range(N):
    heappush(jewels, tuple(map(int, sys.stdin.readline().split())))
for _ in range(K):
    heappush(bags, int(sys.stdin.readline()))

jewels.sort(key=lambda x: x[0])
bags.sort()
print(get_max())
