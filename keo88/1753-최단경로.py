import sys
from heapq import heappop, heappush


def djs(start: int):
    hq = [(0, start)]
    visited = {}

    while hq:
        weight, node = heappop(hq)
        if node in visited:
            continue
        visited[node] = weight

        if node in edges:
            for edge, n_node in edges[node]:
                if n_node not in visited:
                    n_weight = weight + edge
                    heappush(hq, (n_weight, n_node))

    return visited


V, E = map(int, sys.stdin.readline().split())
start = int(input())
edges = {i: [] for i in range(1, V + 1)}
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    edges[u].append((w, v))


ans = djs(start)
for i in range(1, V + 1):
    if i in ans:
        print(ans[i])
    else:
        print('INF')
