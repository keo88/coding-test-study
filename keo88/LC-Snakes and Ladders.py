from collections import deque

class Solution:

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        dq = deque([((n - 1,0), 0)])
        visited = {}

        def getDirection(x: int, n: int):
            return 1 if (n + x) % 2 == 1 else -1
        
        def getPos(num: int, n: int):
            num -= 1
            x = n - (num // n) - 1
            y = num % n if getDirection(x, n) == 1 else n - 1 - (num % n)
            return (x, y)

        dest = getPos(n * n, n)

        while dq:
            pos, depth = dq.popleft()
            if pos in visited:
                continue
            visited[pos] = depth
            x, y = pos
            nPos = []
            for i in range(6):
                dy = getDirection(x, n)
                if 0 <= y + dy < n:
                    y += dy
                else:
                    if x <= 0:
                        break
                    x -= 1
                nPos.append((x, y))
            for nx, ny in nPos:
                if board[nx][ny] != -1:
                    dq.append((getPos(board[nx][ny], n), depth + 1))
                else:
                    dq.append(((nx, ny), depth + 1))
        if dest in visited:
            return visited[dest]
        return -1
