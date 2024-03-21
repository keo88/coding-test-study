def solution(sequence, k):
    answer = [-1, -1]
    l, r = 0, 0
    s = 0
    maxLen = 1000001

    for r in range(len(sequence)):
        s += sequence[r]

        while s > k:
            s -= sequence[l]
            l += 1
        if s == k and maxLen > r - l:
            maxLen = r - l
            answer = [l, r]
    return answer