import sys

K, N = map(int, sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]

st, en = 0, 0x7FFFFFFF + 1


def calc(val):
    cnt = 0
    for i in range(K):
        cnt += arr[i] // val

    return cnt


while st < en:
    mid = (st + en) // 2
    res = calc(mid)
    # print('mid', mid, st, en)

    if res >= N:
        st = mid + 1
        # print('st inc', st)
    else:
        en = mid
        # print('en dec', en)

print(en - 1)
