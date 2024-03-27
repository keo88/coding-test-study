import sys
from collections import deque

N = int(input())
K = int(input())

apples = {}
for i in range(K):
    apples[tuple(map(lambda x: int(x) - 1, sys.stdin.readline().strip().split(' ')))] = 1
changes = []
L = int(input())
for i in range(L):
    temp = sys.stdin.readline().strip().split(' ')

    changes.append((int(temp[0]), temp[1]))

t = 0

dirs = [(0,1), (1,0), (0, -1), (-1, 0)]


def changeDirection(curDir, change):
    ind = dirs.index(curDir)
    if change == 'D':
        return dirs[(ind + 1) % 4]
    else:
        return dirs[(ind - 1) % 4]


ci = 0
pos = (0, 0)
dir = (0, 1)
dq = deque([pos])

for t in range(1, changes[-1][0] + N):
    nextPos = (pos[0] + dir[0], pos[1] + dir[1])
    if nextPos[0] < 0 or nextPos[0] >= N:
        # print(f'crash wall at {nextPos}')
        break
    if nextPos[1] < 0 or nextPos[1] >= N:
        # print(f'crash wall at {nextPos}')
        break

    if nextPos in dq:
        # print(f'crash snake at {nextPos}')
        break

    if nextPos in apples:
        # print(f'apple consumed when {t} at {nextPos}')
        del apples[nextPos]
    else:
        dq.popleft()

    dq.append(nextPos)

    pos = nextPos
    if ci < len(changes) and t == changes[ci][0]:
        dir = changeDirection(dir, changes[ci][1])
        ci += 1


print(t)



