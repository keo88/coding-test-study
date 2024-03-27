import sys
from itertools import combinations
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board, poses, virus = [], [], []
spaces = 0

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for col in range(M):
        if row[col] == 0:
            poses.append((i, col))
            spaces += 1
        elif row[col] == 2:
            virus.append((i, col))
    board.append(row)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
minSpread = 2**31 - 1

for comb in combinations(poses, 3):
    for wallPos in comb:
        board[wallPos[0]][wallPos[1]] = 1

    dq = deque([(v, 0) for v in virus])
    totSpread = -len(virus) + 3
    d = {}

    while dq:
        curPos, depth = dq.popleft()
        if curPos in d:
            continue
        d[curPos] = depth
        totSpread += 1
        if totSpread >= minSpread:
            break

        for i in range(4):
            n_x = curPos[0] + dx[i]
            n_y = curPos[1] + dy[i]
            n_pos = (n_x, n_y)
            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= M:
                continue
            if board[n_x][n_y] >= 1 or n_pos in d:
                continue

            dq.append((n_pos, depth + 1))

    if totSpread < minSpread:
        minSpread = totSpread

    for wallPos in comb:
        board[wallPos[0]][wallPos[1]] = 0

print(spaces - minSpread)
