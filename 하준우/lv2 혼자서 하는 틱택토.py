def solution(board):
    answer = 1
    new = [[],[],[]]
    num1 = num2 = 0
    for i in range(3):
        for j in range(3):
            get = board[i][j]
            if get == 'O':
                new[i].append(1)
                num1 += 1
            elif get == 'X':
                new[i].append(2)
                num2 += 1
            else:
                new[i].append(0)
                
    win1 = False
    if [1,1,1] in new:
        win1 = True
    if (new[0][0] == 1) and (new[1][1] == 1) and (new[2][2] == 1):
        win1 = True
    if (new[0][2] == 1) and (new[1][1] == 1) and (new[2][0] == 1):
        win1 = True
    for i in range(3):
        if (new[0][i] == 1) and (new[1][i] == 1) and (new[2][i] == 1):
            win1 = True
            
    win2 = False
    if [2,2,2] in new:
        win2 = True
    if (new[0][0] == 2) and (new[1][1] == 2) and (new[2][2] == 2):
        win2 = True
    if (new[0][2] == 2) and (new[1][1] == 2) and (new[2][0] == 2):
        win2 = True
    for i in range(3):
        if (new[0][i] == 2) and (new[1][i] == 2) and (new[2][i] == 2):
            win2 = True
            
    if num1 < num2 or num1 - num2 > 1:
        answer = 0
    if win1 and win2:
        answer = 0
    if win1 and num1 -1 != num2:
        answer = 0
    if win2 and num1 != num2:
        answer = 0
    return answer
