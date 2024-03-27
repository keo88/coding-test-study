import sys
from heapq import heappop, heappush

N = int(input())
M = int(input())
intMax = 2 ** 31 - 1
e = {}
for _ in range(M):
    frm, to, cost = map(int, sys.stdin.readline().split())
    if frm == to:
        continue
    if frm - 1 not in e:
        e[frm - 1] = {}
    e[frm - 1][to - 1] = min(cost, e[frm - 1][to - 1]) if to -1 in e[frm - 1] else cost

A, B = map(int, sys.stdin.readline().split())


def bellmanford():
    v = [intMax] * N
    v[A - 1] = 0
    for _ in range(N):
        for frm in e:
            for to in e[frm]:
                val = v[frm] + e[frm][to]
                v[to] = val if val < v[to] else v[to]
    return v[B - 1]


def dijkstra():
    ans = {}
    hq = [(0, A - 1)]

    while hq:
        val, city = heappop(hq)
        if city in ans:
            continue
        ans[city] = val

        if city not in e:
            continue
        for to in e[city]:
            if to not in ans:
                nextVal = e[city][to] + ans[city]
                heappush(hq, (nextVal, to))
    return ans[B - 1]


# print(bellmanford())
print(dijkstra())