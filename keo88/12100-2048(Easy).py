import sys
from collections import deque


def get_board(i: int, j: int, b: list[list[int]]):
    if flag:
        return b[i][j]
    else:
        return b[j][i]


def set_board(i: int, j: int, val: int, b: list[list[int]]):
    if flag:
        b[i][j] = val
    else:
        b[j][i] = val


N = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
dir_ranges = [(N-1, -1, -1), (0, N, 1), (N-1, -1, -1), (0, N, 1)]
flags = [True, True, False, False]
max_v = max(map(max, board))


q = deque([(0, board, max_v)])
while q:
    d, b, M = q.popleft()
    if d == 5:
        max_v = max(max_v, M)
        continue
    for dir in range(4):
        direction = directions[dir]
        dir_range = dir_ranges[dir]
        flag = flags[dir]
        new_b = [[0] * N for _ in range(N)]
        new_M = M
        for i in range(N):
            last_ind = dir_range[0]
            for j in range(*dir_range):
                if get_board(i, j, b) != 0:
                    if get_board(i, j, b) == get_board(i, last_ind, new_b):
                        set_board(i, last_ind, get_board(i, last_ind, new_b) * 2, new_b)
                        new_M = max(new_M, get_board(i, last_ind, new_b))
                        last_ind += dir_range[2]
                    else:
                        if get_board(i, last_ind, new_b) != 0:
                            last_ind += dir_range[2]
                        set_board(i, last_ind, get_board(i, j, b), new_b)
        q.append((d + 1, new_b, new_M))
print(max_v)
