class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        nxt = [[0] * n for _ in range(m)]
        dx = [-1, 0, 1, 1, 1, 0, -1, -1]
        dy = [-1, -1, -1, 0, 1, 1, 1, 0]
        for y in range(m):
            for x in range(n):
                nbrs = 0
                for d in range(8):
                    ny = y + dy[d]
                    nx = x + dx[d]
                    if 0 <= nx < n and 0 <= ny < m and board[y + dy[d]][x + dx[d]] == 1:
                        nbrs += 1
                cs = board[y][x]
                if cs == 1:
                    if 2 <= nbrs < 4:
                        nxt[y][x] = 1
                else:
                    if nbrs == 3:
                        nxt[y][x] = 1
        for y in range(m):
            for x in range(n):
                board[y][x] = nxt[y][x]
                
