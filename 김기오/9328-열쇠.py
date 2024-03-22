import sys
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
T = int(input())


def tryUnlock(door, keys):
    for key in keys:
        if key.upper() == door:
            return True
    return False


for t in range(T):
    N, M = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(N)]
    ans = 0
    
    entries, keys = set(), set()
    for row in range(N):
        if board[row][M - 1] != '*':
            entries.add((row, M - 1))
        if board[row][0] != '*':
            entries.add((row, 0))
    for col in range(M):
        if board[0][col] != '*':
            entries.add((0, col))
        if board[N - 1][col] != '*':
            entries.add((N - 1, col))
    
    keys = set(list(sys.stdin.readline().strip()))
    if '0' in keys:
        keys.remove('0')
    # print('entries', entries)
    # print('keys', keys)
    
    isFoundKey = True
    
    while isFoundKey:
        isFoundKey = False
        
        visited = set()
        for entry in entries:
            
            # for row in range(N):
            #     print(' '.join(board[row]))
            # print()

            dq = deque([entry])
            
            while dq:
                pos = dq.popleft()
                if pos in visited:
                    continue
                visited.add(pos)
                cx, cy = pos
                if board[cx][cy] == '$':
                    ans += 1
                    board[cx][cy] = '.'
                if 'A' <= board[cx][cy] <= 'Z':
                    if tryUnlock(board[cx][cy], keys):
                        board[cx][cy] = '.'
                    else:
                        continue
                elif 'a' <= board[cx][cy] <= 'z':
                    keys.add(board[cx][cy])
                    board[cx][cy] = '.'
                    isFoundKey = True
                
                for i in range(4):
                    nx, ny = cx + dx[i], cy + dy[i]
                    if not (0 <= nx < N and 0 <= ny < M):
                        continue
                    if board[nx][ny] == '*':
                        continue
                    if (nx, ny) in visited:
                        continue
                    dq.append((nx, ny))
                    
    print(ans)