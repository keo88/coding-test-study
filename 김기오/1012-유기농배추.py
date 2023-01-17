import sys
sys.setrecursionlimit(10**4)


def get_adj_pos(rows: int, cols: int, x: int, y: int):
    adjs = []
    if x - 1 >= 0:
        adjs.append((x - 1, y))
    if x + 1 < rows:
        adjs.append((x + 1, y))
    if y - 1 >= 0:
        adjs.append((x, y - 1))
    if y + 1 < cols:
        adjs.append((x, y + 1))
    return adjs


def cascade(N: int, M: int, x: int, y: int, lst: list[(int, int)]):
    lst.remove((x, y))
    target_possible_adjs = get_adj_pos(M, N, x, y)
    for adj in filter(lambda x: x in lst, target_possible_adjs):
        cascade(N, M, adj[0], adj[1], lst)


def get_score(N: int, M: int, points: list[(int, int)]):
    score = 0

    while len(points) > 0:
        point = points[0]
        cascade(N, M, point[0], point[1], points)
        score += 1
    return score


T = int(input())
for t in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    cabbages = list(tuple(map(int, sys.stdin.readline().split())) for _ in range(K))
    if len(cabbages) == 0:
        print(0)
    else:
        ans = get_score(N, M, cabbages)
        print(ans)

