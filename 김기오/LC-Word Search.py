class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        visited = set()
        ans = False

        def dfs(i: int, x: int, y: int):
            if board[x][y] != word[i]:
                return False
            if i + 1 == len(word):
                return True
            
            visited.add((x, y))
            acc = False
            for j in range(4):
                nx, ny = x + dx[j], y + dy[j]
                if 0 <= nx < m and 0 <= ny < n and not (nx, ny) in visited:
                    acc = acc or dfs(i + 1, nx, ny)
            visited.remove((x, y))
            return acc
        
        for x in range(m):
            for y in range(n):
                ans = ans or dfs(0, x, y)
        return ans
