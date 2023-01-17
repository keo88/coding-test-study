def solution(m, n, puddles):
    checkroad = [[1]*m for i in range(n)]
    for i in range(len(puddles)):
        checkroad[puddles[i][1]-1][puddles[i][0]-1] = 0
    check = False
    for i in range(m):
        if check:
            checkroad[0][i] = 0
            continue
        if checkroad[0][i] == 0:
            check = True
    check = False
    for i in range(n):
        if check:
            checkroad[i][0] = 0
            continue
        if checkroad[i][0] == 0:
            check = True
    for i in range(1,n):
        for j in range(1,m):
            if checkroad[i][j]==0:
                continue
            checkroad[i][j] = checkroad[i-1][j] + checkroad[i][j-1]
    return checkroad[n-1][m-1]%1000000007

"""
def goto(m,n,puddles,row,column):
    down = True
    right = True
    if row == m or [row + 1 , column] in puddles:
        down = False
    if column == n or [row , column + 1] in puddles:
        right = False
    if row == m and column == n:
        return 1
    elif not (down or right):
        return 0
    elif down and not(right):
        return goto(m,n,puddles,row+1,column)
    elif not(down) and right:
        return goto(m,n,puddles,row,column+1)
    else:
        return goto(m,n,puddles,row+1,column) + goto(m,n,puddles,row,column+1)

def solution(m, n, puddles):
    return goto(m,n,puddles,1,1)%1000000007
"""
