import sys

N = int(input())
M = int(input())

edges = {}
for i in range(M):
    frm, to, cost = map(int, sys.stdin.readline().split())
    frm -= 1
    to -= 1
    if frm not in edges:
        edges[frm] = {}
    edges[frm][to] = min(edges[frm][to], cost) if to in edges[frm] else cost

def floyd():
    matrix = [[sys.maxsize] * N for _ in range(N)]
    
    for frm in edges:
        for to in edges[frm]:
            matrix[frm][to] = edges[frm][to]
    
    for x in range(N):
        matrix[x][x] = 0
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                matrix[i][j] = min(matrix[i][k] + matrix[k][j], matrix[i][j])
    
    return matrix


from heapq import heappop, heappush
def djs(start: int):
    hq = [(0, start)]
    ans = [sys.maxsize] * N
    
    while hq:
        val, city = heappop(hq)
        if ans[city] <= val:
            continue
        ans[city] = val
        
        if city not in edges:
            continue
        
        for to in edges[city]:
            if ans[to] > val + edges[city][to]:
                heappush(hq, (val + edges[city][to], to))
    
    return list(map(lambda x: x if x < sys.maxsize else 0, ans))


# mat = floyd()
# for i in range(N):
#     print(' '.join(map(lambda x: '0' if x == sys.maxsize else str(x), mat[i])))

for i in range(N):
    print(' '.join(map(str, djs(i))))