import sys
from heapq import heappop, heappush


def djs(start: int):
    hq = [(0, start)]
    ans = {start: 0}

    while hq:
        dist, current_node = heappop(hq)
        if current_node in ans and dist > ans[current_node]:
            continue
        else:
            ans[current_node] = dist

        for t, to in ways[current_node]:
            new_dist = dist + t
            if to not in ans or new_dist < ans[to]:
                heappush(hq, (new_dist, to))

    return ans


N, M, X = map(int, sys.stdin.readline().split())
ways = {}

for i in range(M):
    from_, to_, t = map(int, sys.stdin.readline().split())
    if from_ not in ways:
        ways[from_] = set()
    ways[from_].add((t, to_))

shortest_path = [{}] * (N + 1)
for i in range(1, N + 1):
    shortest_path[i] = djs(i)

max_ans = 0
for i in range(1, N + 1):
    max_ans = max(max_ans, shortest_path[i][X] + shortest_path[X][i])

print(max_ans)
