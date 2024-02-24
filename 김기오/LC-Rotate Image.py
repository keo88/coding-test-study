class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l = n - 1
        for k in range(n // 2):
            firstLine = matrix[k][::-1]
            for t in range(k, n-k):
                matrix[k][t] = matrix[l-t][k]
            for t in range(k, n-k):
                matrix[t][k] = matrix[l-k][t]
            for t in range(k, n-k):
                matrix[l-k][t] = matrix[l-t][l-k]
            for t in range(k, n-k):
                matrix[l-t][l-k] = firstLine[t]
            

        """
        Do not return anything, modify matrix in-place instead.
        """
        
