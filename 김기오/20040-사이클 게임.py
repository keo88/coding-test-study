import sys


def find(x: int):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a: int, b: int):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    elif a_parent > b_parent:
        parent[a_parent] = b_parent


N, M = map(int, sys.stdin.readline().split())
parent = list(range(N))
nodes = [{} for _ in range(N)]
has_stopped = False

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    if find(x) == find(y):
        print(i + 1)
        has_stopped = True
        break
    union(x, y)


if not has_stopped:
    print(0)
