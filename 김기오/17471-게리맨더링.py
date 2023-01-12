import sys
from itertools import combinations, chain

N = int(sys.stdin.readline())

populations = list(map(int, sys.stdin.readline().split()))
adj = list()
for i in range(N):
    adj.append(list(map(int, sys.stdin.readline().split()[1:])))

parent = []
int_max = 2**31 - 1
min_diff = int_max


def powerset(lst):
    return chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1))


def init_parents():
    global parent
    parent = list(range(N + 1))


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def is_union(nodes: tuple):
    init_parents()
    for node in nodes:
        adj_nodes = adj[node - 1]
        for adj_node in adj_nodes:
            if adj_node in nodes:
                union(node, adj_node)

    root = find(nodes[0])
    for node in nodes:
        if find(node) != root:
            return False
    return True


ps = list(powerset(list(range(1, N + 1))))[1:-1]
r = (len(ps) + 1) // 2
for ind in range(r):
    alt_group = ps[-ind - 1]
    if is_union(ps[ind]) and is_union(alt_group):
        population1 = sum(populations[k - 1] for k in ps[ind])
        population2 = sum(populations[k - 1] for k in alt_group)
        min_diff = min(min_diff, abs(population1 - population2))

print(min_diff if min_diff != int_max else -1)
