def solution(sequence):
    
    # Sol 1. 누적합
    acc = [0]
    mult = 1
    for i in range(len(sequence)):
        acc.append(acc[i] + sequence[i] * mult)
        mult *= -1
    return max(acc) - min(acc)
    
    # Sol 2. 카데인
    dp = [[sequence[0], -sequence[0]]]

    for i in range(1, len(sequence)):
        tup = []
        for j in range(2):
            mult = -1 if (i + j) % 2 else 1
            tup.append(max(dp[i - 1][j] + sequence[i] * mult, sequence[i] * mult))
        dp.append(tup)
    return max(item for t in dp for item in t)