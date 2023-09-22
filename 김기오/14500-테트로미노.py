import sys

N, M = map(int, sys.stdin.readline().split(' '))
board = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

checks = [
    [(0,0), (0,1), (0,2), (0, 3)],
    [(0,0), (1,0), (2,0), (3, 0)],
    [(0,0), (1,0), (1,1), (0, 1)],
    [(0,0), (1,0), (2,0), (2, 1)],
    [(0,0), (1,0), (0,1), (0, 2)],
    [(0,0), (0,1), (1,1), (2, 1)],
    [(1,0), (1,1), (1,2), (0, 2)],

    [(0,1), (1,1), (2,0), (2, 1)],
    [(0,0), (1,0), (1,1), (1, 2)],
    [(0,0), (0,1), (1,0), (2, 0)],
    [(0,0), (0,1), (1,2), (0, 2)],

    [(0,1), (1,0), (1,1), (2, 0)],
    [(1,0), (1,1), (0,1), (0, 2)],

    [(0,0), (1,0), (1,1), (2, 1)],
    [(0,0), (1,1), (0,1), (1, 2)],

    [(0,0), (0,1), (1,1), (0, 2)],
    [(0,1), (1,1), (1,0), (2, 1)],
    [(0,1), (1,1), (1,0), (1, 2)],
    [(0,0), (1,0), (2,0), (1, 1)],
]

# for c in checks:
#     display = [
#         ["⬜", "⬜", "⬜", "⬜"],
#         ["⬜", "⬜", "⬜", "⬜"],
#         ["⬜", "⬜", "⬜", "⬜"],
#         ["⬜", "⬜", "⬜", "⬜"],
#     ]
#
#     for i in c:
#         display[i[0]][i[1]] = "⬛"
#
#     for row in display:
#         print(''.join(row))
#     print()
ans = 0

for x, y in [(x, y) for x in range(N) for y in range(M)]:
    for c in checks:

        acc = 0
        for item in c:
            n_x, n_y = x + item[0], y + item[1]
            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= M:
                acc = 0
                continue
            acc += board[n_x][n_y]
        ans = max(ans, acc)
print(ans)


