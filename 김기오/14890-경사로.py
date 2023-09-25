import sys

N, L = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0


for col in range(N):
    last = -1
    acc = 0
    success = True
    accMode = 0
    for i in range(N):
        cur = board[i][col]
        if last == -1 or cur == last:

            if accMode == 0:
                acc += 1
            elif accMode > 0:
                accMode -= 1

        elif accMode:
            success = False
            break

        elif cur == last + 1:
            if acc >= L:
                acc = 1
            else:
                success = False
                break

        elif cur == last - 1:
            accMode = L - 1
            acc = 0

        else:
            success = False
            break

        last = cur
    if not accMode and success:
        ans += 1


for row in range(N):
    last = -1
    acc = 0
    success = True
    accMode = 0
    for i in range(N):
        cur = board[row][i]
        if last == -1 or cur == last:

            if accMode == 0:
                acc += 1
            elif accMode > 0:
                accMode -= 1

        elif accMode:
            success = False
            break

        elif cur == last + 1:
            if acc >= L:
                acc = 1
            else:
                success = False
                break

        elif cur == last - 1:
            accMode = L - 1
            acc = 0

        else:
            success = False
            break

        last = cur
    if not accMode and success:
        ans += 1

print(ans)