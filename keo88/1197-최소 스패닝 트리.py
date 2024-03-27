import sys
from heapq import heappop, heappush


def find(x: int):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a: int, b: int):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def mst(edges: list[(int, int, int)]):
    edges_cnt, ans = 0, 0
    while edges:
        if edges_cnt >= V - 1:
            return ans
        W, S, E = heappop(edges)
        if find(S) == find(E):
            continue
        else:
            union(S, E)
            ans += W
            edges_cnt += 1

    return ans


V, E = map(int, sys.stdin.readline().split())
edges = []
for i in range(E):
    S, E, W = map(int, sys.stdin.readline().split())
    heappush(edges, (W, S, E))
parent = [i for i in range(V + 1)]

print(mst(edges))
