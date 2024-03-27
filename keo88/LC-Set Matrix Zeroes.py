class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        sRows, sCols = set(), set()
        m = len(matrix)
        n = len(matrix[0])
        for y in range(m):
            for x in range(n):
                if matrix[y][x] == 0:
                    sRows.add(y)
                    sCols.add(x)
        for row in sRows:
            for k in range(n):
                matrix[row][k] = 0
        for col in sCols:
            for k in range(m):
                matrix[k][col] = 0

        """
        Do not return anything, modify matrix in-place instead.
        """
        
