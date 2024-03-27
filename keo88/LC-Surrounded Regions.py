class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        Mx = len(board)
        My = len(board[0])

        def dfs(x: int, y: int):
            if board[x][y] != 'O':
                return
            board[x][y] = 'H'
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < Mx and 0 <= ny < My and board[nx][ny] == 'O':
                    dfs(nx, ny)
        for x in range(Mx):
            dfs(x, 0)
            dfs(x, My - 1)
        for y in range(My):
            dfs(0, y)
            dfs(Mx - 1, y)
        
        for x in range(Mx):
            for y in range(My):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'H':
                    board[x][y] = 'O'
        

        
