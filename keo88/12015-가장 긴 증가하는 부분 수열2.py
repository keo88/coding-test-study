import sys
from bisect import bisect_left

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

heads = [arr[0]]

for i in range(1, N):
    j = bisect_left(heads, arr[i])
    if j == len(heads):
        heads.append(arr[i])
    elif heads[j] == arr[i]:
        continue
    else:
        heads[j] = arr[i]

print(len(heads))

