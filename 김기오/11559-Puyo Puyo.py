import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

field = [list(sys.stdin.readline()) for _ in range(12)]


def printField():
    for i in range(12):
        print(' '.join(field[i]))


def popField():
    dq = deque([])
    popped = False
    
    for r, c in ((rx, cx) for rx in range(12) for cx in range(6)):
        
        if field[r][c] == '.':
            continue
        target = field[r][c]
        
        dq.append((r, c))
        visited = set()
        cnt = 0
        
        while dq:
            x, y = dq.popleft()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            cnt += 1
            
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 12 and 0 <= ny < 6 and field[nx][ny] == target:
                    dq.append((nx, ny))
        
        if cnt >= 4:
            popped = True
            for tx, ty in visited:
                field[tx][ty] = '.'
    return popped


def applyGravity():
    for c in range(6):
        shift = 0
        for r in range(11, -1, -1):
            if field[r][c] == '.':
                shift += 1
            else:
                temp = field[r][c]
                field[r][c] = '.'
                field[r + shift][c] = temp



ans = 0

while popField():
    ans += 1
    applyGravity()
print(ans)