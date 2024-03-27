import sys


T = int(input())
for t in range(T):
    N = int(sys.stdin.readline())
    stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    a, b, c, d = 0, 0, stickers[0][0], stickers[1][0]
    for i in range(1, N):
        a, b, c, d = c, d, max(a, b, d) + stickers[0][i], max(a, b, c) + stickers[1][i]
    print(max(c, d))


