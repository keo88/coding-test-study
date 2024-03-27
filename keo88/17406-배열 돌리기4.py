import sys
from itertools import permutations

mat, ops = [], []
N, M, K = map(int, sys.stdin.readline().split())
for row in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))
for op in range(K):
    ops.append(tuple(map(int, sys.stdin.readline().split())))

int_max = 2**31 - 1
min_value = int_max


def inv_rotate_matrix(op: (int, int, int)):
    y, x, d = op[0] - 1, op[1] - 1, op[2]
    for k in range(1, d + 1):
        temp = mat[y - k][x - k]
        for i in range(x - k, x + k):
            mat[y - k][i] = mat[y - k][i + 1]
        for i in range(y - k, y + k):
            mat[i][x + k] = mat[i + 1][x + k]
        for i in range(x + k, x - k, -1):
            mat[y + k][i] = mat[y + k][i - 1]
        for i in range(y + k, y - k, -1):
            if i == y - k + 1:
                mat[i][x - k] = temp
            else:
                mat[i][x - k] = mat[i - 1][x - k]


def rotate_matrix(op: (int, int, int)):
    y, x, d = op[0] - 1, op[1] - 1, op[2]
    for k in range(1, d + 1):
        temp = mat[y - k][x + k]
        for i in range(x + k, x - k, -1):
            mat[y - k][i] = mat[y - k][i - 1]
        for i in range(y - k, y + k):
            mat[i][x - k] = mat[i + 1][x - k]
        for i in range(x - k, x + k):
            mat[y + k][i] = mat[y + k][i + 1]
        for i in range(y + k, y - k, -1):
            if i == y - k + 1:
                mat[i][x + k] = temp
            else:
                mat[i][x + k] = mat[i - 1][x + k]


def calculate_array():
    value = int_max
    for row in range(N):
        value = min(value, sum(mat[row]))
    return value


for orders in permutations(range(K)):
    for ind in orders:
        rotate_matrix(ops[ind])
    min_value = min(min_value, calculate_array())
    for ind in reversed(orders):
        inv_rotate_matrix(ops[ind])

print(min_value)
