from collections import deque


def solution(board):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    N, M = len(board), len(board[0])
    walls = set()
    start, end = (0, 0), (0, 0)
    for r in range(N):
        for c in range(M):
            if board[r][c] == 'D':
                walls.add((r, c))
            elif board[r][c] == 'R':
                start = (r, c)
            elif board[r][c] == 'G':
                end = (r, c)

    # dp = [[] for _ in range(N)]
    # for i in range(N):
    #     for j in range(M):
    #         dp[i].append([-1, -1, -1, -1])

    def getNextPos(pos, ind):
        # if dp[pos[0]][pos[1]][ind] != -1:
        #     return dp[pos[0]][pos[1]][ind]
        curX, curY = pos
        dirX, dirY = dx[ind], dy[ind]
        while True:
            nxtX, nxtY = curX + dirX, curY + dirY
            if nxtX < 0 or nxtX >= N or nxtY < 0 or nxtY >= M:
                break
            if (nxtX, nxtY) in walls:
                break
            curX, curY = nxtX, nxtY
        # dp[pos[0]][pos[1]][ind] = (curX, curY)
        return (curX, curY)

    dq = deque([(start, 0)])
    visited = {}
    goal = False

    while dq:
        pos, depth = dq.popleft()
        if pos in visited:
            continue
        visited[pos] = depth
        if pos == end:
            goal = True
            break

        for i in range(4):
            nxt = getNextPos(pos, i)
            if nxt in visited:
                continue
            dq.append((nxt, depth + 1))

    return visited[end] if goal else -1