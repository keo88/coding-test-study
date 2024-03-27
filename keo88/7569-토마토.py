import sys
from collections import deque


def bfs():
    q = deque(ones)
    zeros_left = zeros_cnt + ones_cnt
    max_d = 0

    while q:
        h, y, x, d = q.popleft()
        if visited[h][y][x]:
            continue
        max_d = max(d, max_d)
        zeros_left -= 1

        visited[h][y][x] = True

        for i in range(6):
            n_x, n_y, n_h = x + dx[i], y + dy[i], h + dh[i]
            if active[i] == 'x':
                if not 0 <= n_x < M:
                    continue
            elif active[i] == 'y':
                if not 0 <= n_y < N:
                    continue
            else:
                if not 0 <= n_h < H:
                    continue
            if box[n_h][n_y][n_x] == -1 or box[n_h][n_y][n_x] == 1:
                continue

            q.append((n_h, n_y, n_x, d + 1))

    return max_d if zeros_left == 0 else -1


dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
active = ['x', 'x', 'y', 'y', 'h', 'h']
M, N, H = map(int, sys.stdin.readline().split())
box, visited = list(), list()
ones, zeros_cnt, ones_cnt = [], 0, 0
for i in range(H):
    box.append([])
    visited.append([])
    for j in range(N):
        box[i].append(list(map(int, sys.stdin.readline().split())))
        visited[i].append([False] * M)
        for k in range(M):
            if box[i][j][k] == 1:
                ones.append((i, j, k, 0))
                ones_cnt += 1
            elif box[i][j][k] == 0:
                zeros_cnt += 1

ans = bfs()
print(ans)
