def solution(sequence):
    answer = 0
    acc = [0]
    mult = 1
    for i in range(len(sequence)):
        acc.append(acc[i] + sequence[i] * mult)
        mult *= -1
    return max(acc) - min(acc)