T = int(input())
intMax = 2 ** 31 - 1
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    board = []
    procs = []
    for row in range(N):
        row_arr = list(map(int, input().split()))
        for col in range(N):
            if row_arr[col] == 1:
                procs.append((row, col))
        board.append(row_arr)

    best_skipped = N
    best = intMax

    def dfs(cur: int, skipped: int, acc: int):
        global best, best_skipped
        if cur == len(procs):
            if best_skipped == skipped:
                if best > acc:
                    best = acc
            elif best_skipped > skipped:
                best_skipped = skipped
                best = acc
            return

        p_x, p_y = procs[cur]
        for d in range(4):
            dirx = dx[d]
            diry = dy[d]
            n_x, n_y = p_x + dirx, p_y + diry
            can_connect = True
            while 0 <= n_x < N and 0 <= n_y < N:
                if board[n_x][n_y] > 0:
                    can_connect = False
                    break
                n_x, n_y = n_x + dirx, n_y + diry

            if can_connect:
                n_x, n_y = p_x + dirx, p_y + diry
                count = 0
                while 0 <= n_x < N and 0 <= n_y < N:
                    board[n_x][n_y] = 2
                    count += 1
                    n_x, n_y = n_x + dirx, n_y + diry

                dfs(cur + 1, skipped, count + acc)

                n_x, n_y = p_x + dirx, p_y + diry
                while 0 <= n_x < N and 0 <= n_y < N:
                    board[n_x][n_y] = 0
                    n_x, n_y = n_x + dirx, n_y + diry
        if skipped + 1 <= best_skipped:
            dfs(cur + 1, skipped + 1, acc)
    dfs(0, 0, 0)
    print(f'#{test_case}', best)