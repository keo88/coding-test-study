import sys
from heapq import heappop, heappush

T =int(input())

for t in range(T):
    k = int(input())
    max_q = []
    min_q = []
    visited = [False] * (k + 1)

    for i in range(k):
        command, num_str = sys.stdin.readline().split()
        num = int(num_str)
        if command == 'I':
            heappush(max_q, (-num, i))
            heappush(min_q, (num, i))
        else:
            if num == 1:
                while max_q and visited[max_q[0][1]]:
                    heappop(max_q)
                if max_q:
                    max_val, key = heappop(max_q)
                    visited[key] = True
            else:
                while min_q and visited[min_q[0][1]]:
                    heappop(min_q)
                if min_q:
                    min_val, key = heappop(min_q)
                    visited[key] = True

    while max_q and visited[max_q[0][1]]:
        heappop(max_q)
    while min_q and visited[min_q[0][1]]:
        heappop(min_q)
    if max_q:
        print(-max_q[0][0], min_q[0][0])
    else:
        print('EMPTY')
