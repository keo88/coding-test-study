class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        yMin, yMax = 0, len(matrix) - 1
        xMin, xMax = 0, len(matrix[0]) - 1

        dI = 0
        curX, curY = 0, 0
        ans = []
        cap = len(matrix) * len(matrix[0])
        while True:
            if dI == 0:
                while curX < xMax:
                    ans.append(matrix[curY][curX])
                    curX += 1
                yMin += 1
            elif dI == 1:
                while curY < yMax:
                    ans.append(matrix[curY][curX])
                    curY += 1
                xMax -= 1
            elif dI == 2:
                while curX > xMin:
                    ans.append(matrix[curY][curX])
                    curX -= 1
                yMax -= 1
            else:
                while curY > yMin:
                    ans.append(matrix[curY][curX])
                    curY -= 1
                xMin += 1
            dI = (dI + 1) % 4
            if len(ans) == cap - 1:
                ans.append(matrix[curY][curX])
                break
        return ans



