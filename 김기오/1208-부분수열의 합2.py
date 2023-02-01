import sys
from itertools import combinations
from heapq import heappop, heappush


def powerset(ints: list[int], rev: bool):
    hq = [0]
    k = -1 if rev else 1
    for i in range(1, len(ints) + 1):
        for c in combinations(ints, i):
            heappush(hq, k * sum(c))
    return hq


def main():
    ans = -1 if S == 0 else 0
    rs, ls = -heappop(ra), heappop(la)

    while True:
        if rs + ls == S:
            c1, c2 = 1, 1
            while ra and ra[0] == -rs:
                rs = -heappop(ra)
                c1 += 1
            while la and la[0] == ls:
                ls = heappop(la)
                c2 += 1
            ans += c1 * c2
            if not ra and not la:
                break
            if ra:
                rs = -heappop(ra)
            if la:
                ls = heappop(la)
        elif ls + rs < S:
            if la:
                ls = heappop(la)
            else:
                break
        else:
            if ra:
                rs = -heappop(ra)
            else:
                break

    return ans


N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
la, ra = powerset(arr[:len(arr) // 2], False), powerset(arr[len(arr) // 2:], True)
print(main())
