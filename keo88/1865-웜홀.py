import sys


def bellman_iter(ans: dict[int, int], edges: dict[int, list[(int, int)]]):
    updated = False
    for node in edges:
        if node not in ans:
            continue
        base = ans[node]
        for edge, n_node in edges[node]:
            n_edge = base + edge
            if n_node not in ans or n_edge < ans[n_node]:
                updated = True
                ans[n_node] = n_edge
    return updated


def bellman_ford(start: int, v: int, edges: dict[int, list[(int, int)]]):
    ans = {start: 0}
    for _ in range(v - 1):
        bellman_iter(ans, edges)

    if bellman_iter(ans, edges):
        return False
    return True


T = int(input())
for t in range(T):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        start, end, wei = map(int, sys.stdin.readline().split())
        edges[start].append((wei, end))
        edges[end].append((wei, start))
    for _ in range(W):
        start, end, wei = map(int, sys.stdin.readline().split())
        edges[start].append((-wei, end))

    edges[N + 1] = [(0, i) for i in range(1, N+1)]
    res = bellman_ford(N + 1, N + 1, edges)
    if res:
        print('NO')
    else:
        print('YES')
