import sys
from collections import deque

N, M = map(int, input().split())
b = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
targets = [tuple(map(lambda x: int(x) - 1, sys.stdin.readline().split())) for _ in range(M)]
camps = []

for row in range(N):
    for col in range(N):
        if b[row][col] == 1:
            camps.append((row, col))

persons = {}
t = 1

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

maxInt = 2**31 -1


def bfs(start: (int, int), dest: list[(int, int)]):
    dq = deque([(start, 0)])
    d = {}
    min_dest = maxInt
    ans = []

    while dq:
        pos, depth = dq.popleft()
        if pos in d:
            continue
        d[pos] = depth
        if pos in dest:
            if depth > min_dest:
                break
            else:
                min_dest = depth
                ans.append(pos)

        for i in range(4):
            n_x, n_y = pos[0] + dx[i], pos[1] + dy[i]
            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                continue
            if b[n_x][n_y] > 1:
                continue
            n_pos = (n_x, n_y)
            if n_pos in d:
                continue
            dq.append((n_pos, depth + 1))
    return ans


while True:
    arrived = []

    # 1. move.
    for i in persons:
        p_pos, p_target = persons[i]
        adjs = []
        for j in range(4):
            n_x, n_y = p_pos[0] + dx[j], p_pos[1] + dy[j]
            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                continue
            if b[n_x][n_y] > 1:
                continue

            adjs.append((n_x, n_y))
        nearest_adjs = bfs(p_target, adjs)

        flag = False
        for j in range(4):
            n_x, n_y = p_pos[0] + dx[j], p_pos[1] + dy[j]
            for adj in nearest_adjs:
                if adj == (n_x, n_y):
                    nearest_adj = adj
                    flag = True
                    break
            if flag:
                break
        if nearest_adj == p_target:
            arrived.append(i)
        persons[i] = (nearest_adj, p_target)

    # 2. check stopped.
    for arrived_ind in arrived:
        _, p_target = persons[arrived_ind]
        b[p_target[0]][p_target[1]] = 2
        del persons[arrived_ind]

    # 3. add person.
    if t <= M:
        target = targets[t - 1]
        nearest_camps = bfs(target, camps)

        min_x = min(map(lambda x: x[0], nearest_camps))
        nearest_camps = list(filter(lambda x: x[0] == min_x, nearest_camps))
        if len(nearest_camps) > 1:
            min_y = min(map(lambda x: x[1], nearest_camps))
            nearest_camps = list(filter(lambda x: x[1] == min_y, nearest_camps))
        base_camp = nearest_camps[0]

        b[base_camp[0]][base_camp[1]] = 2

        persons[t] = (base_camp, target)

    # print('t', t)
    # for i in range(N):
    #     print(' '.join(map(str, b[i])))

    if len(persons) == 0:
        break
    t += 1

print(t)
