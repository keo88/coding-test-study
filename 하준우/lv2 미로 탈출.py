def find(maps,first,end,white,garo,sero,stack):
    if (first[0] < 0) or (first[0] >= garo) or (first[1] < 0) or (first[1] >= sero):
        return 99999
    if maps[first[0]][first[1]] == 'X':
        return 99999
    if white[first[0]][first[1]] > first[2]:
        white[first[0]][first[1]] = first[2]
        stack.append([first[0]+1,first[1],first[2]+1])
        stack.append([first[0],first[1]+1,first[2]+1])
        stack.append([first[0]-1,first[1],first[2]+1])
        stack.append([first[0],first[1]-1,first[2]+1])
    else:
        return 99999
    
def solution(maps):
    answer = 0
    start = []
    lever = []
    exit = []
    garo = len(maps)
    sero = len(maps[0])
    for i in range(garo):
        for j in range(sero):
            if maps[i][j] == 'S':
                start = [i,j]
            elif maps[i][j] == 'L':
                lever = [i,j]
            elif maps[i][j] == 'E':
                exit = [i,j]
                
                
    white = []
    stack = [[start[0],start[1],0]]
    for i in range(garo):
        white.append([99999]*sero)
    while len(stack) != 0:
        find(maps,[stack[0][0],stack[0][1],stack[0][2]],[lever[0],lever[1]],white,garo,sero,stack)
        stack.pop(0)
    if white[lever[0]][lever[1]] == 99999:
        return -1
    else:
        answer += white[lever[0]][lever[1]]
        
        
    white = []
    stack = [[lever[0],lever[1],0]]
    for i in range(garo):
        white.append([99999]*sero)
    while len(stack) != 0:
        find(maps,[stack[0][0],stack[0][1],stack[0][2]],[lever[0],lever[1]],white,garo,sero,stack)
        stack.pop(0)
    if white[exit[0]][exit[1]] == 99999:
        return -1
    else:
        answer += white[exit[0]][exit[1]]
        
    return answer
'''
def find(maps,first,end,white,garo,sero,time):
    if (first[0] < 0) or (first[0] >= garo) or (first[1] < 0) or (first[1] >= sero):
        return 99999
    if maps[first[0]][first[1]] == 'X':
        return 99999
    if white[first[0]][first[1]] > time:
        white[first[0]][first[1]] = time
        if first[0] == end[0] and first[1] == end[1]:
            return 0
    else:
        return 99999
    return min(find(maps,[first[0]+1,first[1]],end,white,garo,sero,time+1),find(maps,[first[0],first[1]+1],end,white,garo,sero,time+1),find(maps,[first[0]-1,first[1]],end,white,garo,sero,time+1),find(maps,[first[0],first[1]-1],end,white,garo,sero,time+1))
    
def solution(maps):
    answer = 0
    start = []
    lever = []
    exit = []
    garo = len(maps)
    sero = len(maps[0])
    for i in range(garo):
        for j in range(sero):
            if maps[i][j] == 'S':
                start = [i,j]
            elif maps[i][j] == 'L':
                lever = [i,j]
            elif maps[i][j] == 'E':
                exit = [i,j]
    white = []
    for i in range(garo):
        white.append([99999]*sero)
    find(maps,[start[0],start[1]],[lever[0],lever[1]],white,garo,sero,0)
    if white[lever[0]][lever[1]] == 99999:
        return -1
    else:
        answer += white[lever[0]][lever[1]]
    white = []
    for i in range(garo):
        white.append([99999]*sero)
    find(maps,[lever[0],lever[1]],[exit[0],exit[1]],white,garo,sero,0)
    if white[exit[0]][exit[1]] == 99999:
        return -1
    else:
        answer += white[exit[0]][exit[1]]
    return answer




def find1(maps,first,end,white,garo,sero,stack):
    if not((first[0]+1 < 0) or (first[0]+1 >= garo) or (first[1] < 0) or (first[1] >= sero) or maps[first[0]+1][first[1]] == 'X' or (white[first[0]+1][first[1]] < white[first[0]][first[1]] + 1)):
        white[first[0]+1][first[1]] = white[first[0]][first[1]] + 1
        stack.append([first[0]+1,first[1]])
    if not((first[0] < 0) or (first[0] >= garo) or (first[1]+1 < 0) or (first[1]+1 >= sero) or maps[first[0]][first[1]+1] == 'X' or (white[first[0]][first[1]+1] < white[first[0]][first[1]] + 1)):
        white[first[0]][first[1]+1] = white[first[0]][first[1]] + 1
        stack.append([first[0],first[1]+1])
    if not((first[0]-1 < 0) or (first[0]-1 >= garo) or (first[1] < 0) or (first[1] >= sero) or maps[first[0]-1][first[1]] == 'X' or (white[first[0]-1][first[1]] < white[first[0]][first[1]] + 1)):
        white[first[0]-1][first[1]] = white[first[0]][first[1]] + 1
        stack.append([first[0]-1,first[1]])
    if not((first[0] < 0) or (first[0] >= garo) or (first[1]-1 < 0) or (first[1]-1 >= sero) or maps[first[0]][first[1]-1] == 'X' or (white[first[0]][first[1]-1] < white[first[0]][first[1]] + 1)):
        white[first[0]][first[1]-1] = white[first[0]][first[1]] + 1
        stack.append([first[0],first[1]-1])
    if white[end[0]][end[1]] != 99999:
        stack = [99999]
    
    
    
def solution1(maps):
    answer = 0
    start = []
    lever = []
    exit = []
    garo = len(maps)
    sero = len(maps[0])
    for i in range(garo):
        for j in range(sero):
            if maps[i][j] == 'S':
                start = [i,j]
            elif maps[i][j] == 'L':
                lever = [i,j]
            elif maps[i][j] == 'E':
                exit = [i,j]
                
                
    white = []
    stack = [[start[0],start[1]]]
    ite = 400000
    for i in range(garo):
        white.append([99999]*sero)
    white[start[0]][start[1]] = 0
    while len(stack) != 0 and ite != 0:
        find(maps,[stack[0][0],stack[0][1]],[lever[0],lever[1]],white,garo,sero,stack)
        stack.pop(0)
        ite -= 1
    if white[lever[0]][lever[1]] == 99999:
        return -1
    else:
        answer += white[lever[0]][lever[1]]
        
        
    white = []
    stack = [[lever[0],lever[1]]]
    ite = 400000
    for i in range(garo):
        white.append([99999]*sero)
    white[lever[0]][lever[1]] = 0
    while len(stack) != 0 and ite != 0:
        find(maps,[stack[0][0],stack[0][1]],[lever[0],lever[1]],white,garo,sero,stack)
        stack.pop(0)
        ite -= 1
    if white[exit[0]][exit[1]] == 99999:
        return -1
    else:
        answer += white[exit[0]][exit[1]]
        
    return answer
'''
