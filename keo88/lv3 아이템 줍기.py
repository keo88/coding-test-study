from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    bound = 102
    ter = [([0] * bound) for _ in range(bound)]

    for r in rectangle:
        for x in range(2 * r[0], 2 * r[2] + 1):
            for y in range(2 * r[1], 2 * r[3] + 1):
                ter[x][y] = 1

    q = deque([(characterX * 2, characterY * 2, 0)])
    dp = {}
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    itemX *= 2
    itemY *= 2

    def bfs():
        while q:
            cur_x, cur_y, d = q.popleft()
            if cur_x == itemX and cur_y == itemY:
                return d
            if (cur_x, cur_y) in dp:
                continue
            dp[(cur_x, cur_y)] = d
            # if len(rectangle) == 4 and rectangle[1][0] == 3:
            #     print(f'-----cur_x {cur_x // 2} cur_y {cur_y // 2}')

            for i in range(4):
                n_x, n_y = cur_x + dx[i] * 2, cur_y + dy[i] * 2
                # print(f'n_x {n_x} n_y {n_y} d {d}')
                if n_x < 0 or n_x >= bound or n_y < 0 or n_y >= bound:
                    continue
                if ter[n_x][n_y] != 1:
                    continue
                if dx[i] != 0:
                    # print(f' check ter[cur_x + dx[i]][cur_y + 1] {ter[cur_x + dx[i]][cur_y + 1]} n_y {ter[cur_x + dx[i]][cur_y - 1]}')
                    if ter[cur_x + dx[i]][cur_y + 1] + ter[cur_x + dx[i]][cur_y - 1] != 1:
                        continue
                else:
                    # print(f' check ter[cur_x + 1][cur_y + dy[i]] {ter[cur_x + 1][cur_y + dy[i]]} n_y {ter[cur_x - 1][cur_y + dy[i]]}')
                    if ter[cur_x + 1][cur_y + dy[i]] + ter[cur_x - 1][cur_y + dy[i]] != 1:
                        continue
                q.append((n_x, n_y, d + 1))

    return bfs()