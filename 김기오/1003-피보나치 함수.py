import sys

N = int(input())
memo = [(1, 0), (0, 1)]
memo_len = 2


def get_memo(n: int):
    global memo_len

    if n >= memo_len:
        n_2 = get_memo(n - 2)
        n_1 = get_memo(n - 1)
        memo.append((n_2[0] + n_1[0], n_2[1] + n_1[1]))
        memo_len += 1
        return memo[n]
    else:
        return memo[n]


for i in range(N):
    n = int(sys.stdin.readline())
    k = get_memo(n)
    print(' '.join(map(str, memo[n])))
