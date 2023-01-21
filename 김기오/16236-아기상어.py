import sys
from collections import deque

N = int(input())

world = []
cur_pos = (-1, -1)
for i in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))
    for j in range(N):
        if world[i][j] == 9:
            cur_pos = (j, i)
            world[i][j] = -1

size, eat_cnt, seconds = 2, 0, 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def get_world(x: int, y: int):
    return world[y][x]


def bfs():
    global cur_pos, eat_cnt, size
    q = deque([(cur_pos, 0)])
    target_depth = N ** 2
    targets, visited = [], {}
    fish_found = False

    while q:
        pos, depth = q.popleft()
        if pos in visited:
            continue
        if depth > target_depth:
            break

        item = get_world(*pos)

        if item > size:
            continue
        elif 0 < item < size:
            fish_found = True
            target_depth = depth
            targets.append(pos)
            visited[pos] = 1
            continue

        visited[pos] = 1

        for d in range(4):
            new_pos = pos[0] + dx[d], pos[1] + dy[d]
            if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N:
                q.append((new_pos, depth + 1))

    if fish_found:
        min_y = min(targets, key=lambda x: x[1])
        min_y_targets = filter(lambda y: y[1] == min_y[1], targets)
        min_x = min(min_y_targets, key=lambda x: x[0])

        world[min_x[1]][min_x[0]] = -1
        world[cur_pos[1]][cur_pos[0]] = 0

        cur_pos = min_x
        eat_cnt += 1
        if eat_cnt == size:
            size += 1
            eat_cnt = 0
        return target_depth
    else:
        return -1


while True:
    seconds_taken_round = bfs()
    if seconds_taken_round == -1:
        print(seconds)
        break
    else:
        seconds += seconds_taken_round
        # for i in range(N):
        #     print(' '.join(map(str, world[i])))
        # print(f'Total seconds : {seconds}\nSeconds this round: {seconds_taken_round}\nSize: {size}')
