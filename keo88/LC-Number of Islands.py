class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        id = 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        Mx = len(grid)
        My = len(grid[0])

        def dfs(x: int, y: int, tid: str):
            if grid[x][y] == tid:
                return
            grid[x][y] = tid
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < Mx and 0 <= ny < My and grid[nx][ny] == '1':
                    dfs(nx, ny, tid)
        
        for (x, y) in ((a, b) for a in range(Mx) for b in range(My)):
            if grid[x][y] == '1':
                id += 1
                dfs(x, y, str(id))
        
        return id - 1
