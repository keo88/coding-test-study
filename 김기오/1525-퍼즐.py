import sys
from collections import deque


def toMask(puzzle: list[int]):
    val, i = 0, 0
    for item in puzzle:
        val |= (item << i)
        i += 4
    return val


def isDone(puzzle: list[int]):
    for i in range(8):
        if puzzle[i] != i + 1:
            return False
    return True


arr, dp = [], {}
pos_lst = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [2, 4, 8],
    [3, 7],
    [4, 6, 8],
    [5, 7]
]
init_0 = 0
for i in range(3):
    arr.extend(list(map(int, sys.stdin.readline().split())))
for i in range(len(arr)):
    if arr[i] == 0:
        init_0 = i
        break


def bfs():
    q = deque([(arr, init_0, 0)])
    while q:
        state, zero_ind, d = q.popleft()
        m = toMask(state)
        if m in dp:
            continue
        if isDone(state):
            return d
        dp[m] = d

        pos = pos_lst[zero_ind]
        for i in range(len(pos)):
            new_arr = state.copy()
            new_arr[zero_ind] = new_arr[pos[i]]
            new_arr[pos[i]] = 0
            n_m = toMask(new_arr)
            if n_m in dp:
                continue
            q.append((new_arr, pos[i], d + 1))
    return -1


print(bfs())
