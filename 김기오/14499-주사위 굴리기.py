import sys

N, M, x, y, K = map(int, sys.stdin.readline().split(' '))
board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split(' '))))
commands = list(map(int, sys.stdin.readline().split(' ')))


dice = (0, 0, 0, 0, 0, 0)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def rotate(command, dice):
    if command == 1:
        dice = (dice[3], dice[1], dice[0], dice[5], dice[4], dice[2])
    elif command == 2:
        dice = (dice[2], dice[1], dice[5], dice[0], dice[4], dice[3])
    elif command == 3:
        dice = (dice[4], dice[0], dice[2], dice[3], dice[5], dice[1])
    elif command == 4:
        dice = (dice[1], dice[5], dice[2], dice[3], dice[0], dice[4])
    else:
        raise KeyError('Wrong command')
    return dice


for c in commands:
    n_x, n_y = x + dx[c-1], y + dy[c-1]
    if n_x < 0 or n_x >= N:
        continue
    elif n_y < 0 or n_y >= M:
        continue

    dice = rotate(c, dice)
    if board[n_x][n_y] == 0:
        board[n_x][n_y] = dice[5]
    elif board[n_x][n_y] != 0:
        dice = (dice[0], dice[1], dice[2], dice[3], dice[4]) + (board[n_x][n_y], )
        board[n_x][n_y] = 0

    print(dice[0])

    x = n_x
    y = n_y
