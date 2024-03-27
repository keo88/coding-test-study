import sys


def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        count[a] += count[b]
        count[b] = 0
    elif a > b:
        parent[a] = b
        count[b] += count[a]
        count[a] = 0


def ccw(p1: (int, int), p2: (int, int), p3: (int, int)):
    return p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1] - (p2[0] * p1[1] + p3[0] * p2[1] + p1[0] * p3[1])


def check(p1: (int, int), p2: (int, int), p3: (int, int), p4: (int, int)):
    res1 = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    res2 = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if res1 == 0 and res2 == 0:
        k = 1 if p1[0] == p2[0] else 0
        if max(min(p1[k], p2[k]), min(p3[k], p4[k])) <= min(max(p1[k], p2[k]), max(p3[k], p4[k])):
            return True
        else:
            return False
    elif res1 <= 0 and res2 <= 0:
        return True
    else:
        return False


N = int(input())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
parent = list(range(N))
count = [1] * N

for i in range(N):
    for j in range(i):
        if check((lines[i][0], lines[i][1]), (lines[i][2], lines[i][3]), (lines[j][0], lines[j][1]), (lines[j][2], lines[j][3])):
            union(j, i)

max_count = 0
groups_count = 0
for i in range(N):
    if count[i] > 0:
        groups_count += 1
    max_count = max(max_count, count[i])
print(groups_count, max_count, sep='\n')

