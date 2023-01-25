import sys
from heapq import heappush, heappop


def djs(s_node: int):
    hq = [(0, s_node)]
    visited = {}

    while hq:
        cost, node = heappop(hq)
        if node in visited:
            continue
        visited[node] = cost

        for e, n_node in edges[node]:
            n_cost = cost + e
            if n_node not in visited or n_cost < visited[node]:
                heappush(hq, (n_cost, n_node))

    return visited


N, E = map(int, sys.stdin.readline().split())
edges = {i: [] for i in range(1, N + 1)}

for i in range(E):
    start, end, val = map(int, sys.stdin.readline().split())
    edges[start].append((val, end))
    edges[end].append((val, start))

from_, to_ = map(int, sys.stdin.readline().split())

dist1 = djs(1)
dist2 = djs(from_)
dist3 = djs(to_)

try:
    val1 = dist1[from_] + dist2[to_] + dist3[N]
    val2 = dist1[to_] + dist3[from_] + dist2[N]
    print(min(val1, val2))
except KeyError:
    print(-1)
