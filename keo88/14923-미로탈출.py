import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
Hy, Hx = map(int, sys.stdin.readline().split())
Ey, Ex = map(int, sys.stdin.readline().split())

world, walls = [], []

for row in range(N):
    world.append([])
    j = 0
    for col in map(int, sys.stdin.readline().split()):
        if col == 1:
            walls.append((j, row))
        world[row].append(col)
        j += 1

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def dfs(start: (int, int), visited: dict):
    q = deque([(start, 0)])

    while q:
        node, d = q.popleft()
        if node in visited:
            continue
        visited[node] = d

        for i in range(4):
            n_x, n_y = node[0] + dx[i], node[1] + dy[i]
            n_node = n_x, n_y
            if n_node in visited:
                continue
            elif n_x >= M or n_x < 0 or n_y >= N or n_y < 0:
                continue
            elif world[n_y][n_x] != 0:
                continue
            else:
                q.append((n_node, d + 1))


visitedE, visitedH = {}, {}
dfs((Ex - 1, Ey - 1), visitedE)
dfs((Hx - 1, Hy - 1), visitedH)


int_max = 2**31 - 1
ans = int_max if (Hx - 1, Hy - 1) not in visitedE else visitedE[(Hx - 1, Hy - 1)]

for wall in walls:
    min_h_val, min_e_val = int_max, int_max
    min_h_ind, min_e_ind = (-1, -1), (-1, -1)
    for i in range(4):
        n_x, n_y = wall[0] + dx[i], wall[1] + dy[i]
        n_wall = n_x, n_y
        if n_wall in visitedE:
            if min_e_val > visitedE[n_wall]:
                min_e_ind = n_wall
                min_e_val = visitedE[n_wall]
        if n_wall in visitedH:
            if min_h_val > visitedH[n_wall]:
                min_h_ind = n_wall
                min_h_val = visitedH[n_wall]

    if min_h_ind == (-1, -1) or min_e_ind == (-1, -1) or min_e_ind == min_h_ind:
        continue

    ans = min(min_e_val + min_h_val + 2, ans)


print(ans if ans != int_max else -1)

