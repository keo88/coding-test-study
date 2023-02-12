import sys


def bishop(row: int, col: int, count: int):
    if col >= n:
        row += 1
        col = 1 if col % 2 == 0 else 0
    if row >= n:
        return count

    ret = count
    if board[row][col] == 1 and l[row + col] and r[row - col + n - 1]:
        l[row + col] = False
        r[row - col + n - 1] = False
        ret = bishop(row, col + 2, count + 1)
        l[row + col] = True
        r[row - col + n - 1] = True

    ret = max(ret, bishop(row, col + 2, count))
    return ret


n = int(input())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
l, r = [True] * (2 * n), [True] * (2 * n)

a = bishop(0, 0, 0)
b = bishop(0, 1, 0) if n != 1 else 0
print(a + b)
