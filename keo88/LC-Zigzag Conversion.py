class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [[] for _ in range(numRows)]
        rowInd = 0
        isWritingVert = True
        for ch in s:
            rows[rowInd].append(ch)
            if isWritingVert:
                if rowInd == numRows - 1:
                    rowInd -= 1
                    isWritingVert = False
                else:
                    rowInd += 1
            else:
                if rowInd == 0:
                    isWritingVert = True
                    rowInd += 1
                else:
                    rowInd -= 1
        # print(''.join(''.join(row) for row in rows), sep='')
        return ''.join(''.join(row) for row in rows)
