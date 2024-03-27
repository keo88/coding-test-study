import sys


def x():
    i, j = 0, 0
    s, min_len = arr[0], int_max
    while j < len(arr):
        while s < S:
            j += 1
            if j == len(arr):
                return min_len
            s += arr[j]
            # print(f'Add Phase i: {i} j: {j} s: {s}')
        while s - arr[i] >= S:
            s -= arr[i]
            i += 1
            # print(f'Reduce Phase i: {i} j: {j} s: {s}')
        min_len = min(min_len, j - i + 1)
        # print(f'Min Len Cal Phase i: {i} j: {j} s: {s}')
        if j == len(arr) - 1:
            break

        if i == j:
            j += 1
            s += arr[j]
        s -= arr[i]
        i += 1
    return min_len


int_max = 2**31 - 1
N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = x()
if ans == int_max:
    print(0)
else:
    print(ans)
