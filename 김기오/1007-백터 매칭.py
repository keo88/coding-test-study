import sys
from itertools import combinations


T = int(input())
for t in range(T):
    n = int(sys.stdin.readline())
    points = []
    for p in range(n):
        points.append(tuple(map(int, sys.stdin.readline().split())))

    min_val = float('infinity')
    combs = list(combinations(range(n), n // 2))
    for c in combs[:len(combs) // 2]:
        pos_x, pos_y = 0, 0
        neg_x, neg_y = 0, 0
        for i in range(n):
            if i in c:
                pos_x += points[i][0]
                pos_y += points[i][1]
            else:
                neg_x += points[i][0]
                neg_y += points[i][1]

        x, y = pos_x - neg_x, pos_y - neg_y
        min_val = min(min_val, x ** 2 + y ** 2)

    print(min_val ** 0.5)
