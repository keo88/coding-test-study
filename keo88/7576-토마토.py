import sys
from collections import deque


def bfs():
    q = deque(ones)
    zeros_left = zeros_cnt + ones_cnt
    max_d = 0

    while q:
        y, x, d = q.popleft()
        if box[y][x] > 1:
            continue
        max_d = max(d, max_d)
        zeros_left -= 1
        box[y][x] = d

        for i in range(4):
            n_x, n_y = x + dx[i], y + dy[i]
            if active[i] == 'x':
                if not 0 <= n_x < M:
                    continue
            else:
                if not 0 <= n_y < N:
                    continue
            if box[n_y][n_x] == -1 or box[n_y][n_x] >= 1:
                continue

            q.append((n_y, n_x, d + 1))

    return max_d - 1 if zeros_left == 0 else -1


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
active = ['x', 'x', 'y', 'y']
M, N = map(int, sys.stdin.readline().split())
box = list()
ones, zeros_cnt, ones_cnt = [], 0, 0
for i in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))
    for j in range(M):
        if box[i][j] == 1:
            ones.append((i, j, 1))
            ones_cnt += 1
        elif box[i][j] == 0:
            zeros_cnt += 1

ans = bfs()
print(ans)
