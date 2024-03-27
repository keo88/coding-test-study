import sys
from collections import deque


def get_world_pos(x, y):
    return world[y][x]


def move_ball(ball: (int, int), direction: (int, int), obstacles: list[(int, int)]=None):
    if obstacles:
        removals = []
        for i in range(len(obstacles)):
            if (obstacles[i][0] * ball[0] > direction[0] * ball[0] and obstacles[i][1] == ball[1]) or (obstacles[i][1] * ball[1] > direction[1] * ball[1] and obstacles[i][0] == ball[0]):
                continue
            else:
                removals.append(i)
        for i in removals:
            obstacles.pop(i)
        if len(obstacles) == 0:
            obstacles = None

    cur_pos, hit_o = ball, False
    while True:
        next_pos = cur_pos[0] + direction[0], cur_pos[1] + direction[1]
        if get_world_pos(*next_pos) == '.':
            if obstacles and next_pos in obstacles:
                break
            cur_pos = next_pos
            continue
        elif get_world_pos(*next_pos) == '#':
            break
        elif get_world_pos(*next_pos) == 'O':
            hit_o = True
            cur_pos = -1, -1
            break

    return hit_o, cur_pos


def move_balls(r: (int, int), b: (int, int), dx: int, dy: int):
    if dx * r[0] + dy * r[1] >= dx * b[0] + dy * b[1]:
        # r이 먼저.
        r_hit, r_next = move_ball(r, (dx, dy))
        b_hit, b_next = move_ball(b, (dx, dy), [r_next] if not r_hit else None)
        if b_hit:
            return -1, r_next, b_next
        elif r_hit:
            return 1, r_next, b
    else:
        b_hit, b_next = move_ball(b, (dx, dy))
        if b_hit:
            return -1, r, b_next
        r_hit, r_next = move_ball(r, (dx, dy), [b_next] if not b_hit else None)
        if r_hit:
            return 1, r_next, b_next

    if r_next == r and b_next == b:
        return -1, r, b
    else:
        if b_hit:
            return -1, r_next, b_next
        elif r_hit:
            return 1, r_next, b_next
        elif (r_next, b_next) in visited:
            return -1, r_next, b_next
        else:
            visited[(r_next, b_next)] = 1
            return 0, r_next, b_next


def bfs():
    queue = deque([(r_pos, b_pos, 1)])

    while queue:
        r, b, depth = queue.popleft()
        if depth == 11:
            return -1
        for i in range(4):
            flag, r_next, b_next = move_balls(r, b, dx[i], dy[i])
            if flag == 1:
                return depth
            elif flag == 0:
                queue.append((r_next, b_next, depth + 1))
    return -1


N, M = map(int, sys.stdin.readline().split())
world, r_pos, b_pos, o_pos = [], (0, 0), (0, 0), (0, 0)
for i in range(N):
    world.append(list(sys.stdin.readline().strip()))
    for j in range(1, M-1):
        if world[i][j] == 'R':
            r_pos = (j, i)
            world[i][j] = '.'
        elif world[i][j] == 'B':
            b_pos = (j, i)
            world[i][j] = '.'
        elif world[i][j] == 'O':
            o_pos = (j, i)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = dict()

print(bfs())
