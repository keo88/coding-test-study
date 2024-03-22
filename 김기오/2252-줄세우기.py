import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
d = {}
degree = [0] * N

for _ in range(M):
    left, right = map(int, sys.stdin.readline().split())
    left -= 1
    right -= 1
    if left not in d:
        d[left] = set()
    if right not in d[left]:
        d[left].add(right)
        degree[right] += 1

entries = []
for i in range(N):
    if degree[i] == 0:
        entries.append(i)
        degree[i] += 1

dq = deque(entries)

ans = []
while dq:
    item = dq.popleft()
    degree[item] -= 1
    if degree[item] <= 0:
        ans.append(item + 1)
        if item not in d:
            continue
        for nxt in d[item]:
            dq.append(nxt)

print(' '.join(map(str, ans)))
