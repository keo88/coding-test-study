def getFactorsSmart(Max):
    # 가장 작은 소인수
    minFactor = [x for x in range(Max+1)]
    minFactor[0] = 0
    minFactor[1] = 1

    sqrtn = int(Max ** 0.5)

    for i in range(2, sqrtn+1):
        if minFactor[i] == i:
            for j in range(i*i, Max+1, i):
                if minFactor[j] == j:
                    minFactor[j] = i

    # minFactorPower[i] = i 의 소인수 분해에는 minFactor[i]의 몇승이 포함되는지
    minFactorPower = [0] * (Max + 1)

    # factors[i] = i 가 가진 약수의 개수
    factors = [0] * (Max + 1)
    # 1의 약수는 1개
    factors[1] = 1

    for i in range(2, Max+1):
        # 소수인 경우
        if minFactor[i] == i:
            # i ** 1 승
            minFactorPower[i] = 1
            # 소수 [1, i] -> 2개
            factors[i] = 2
        else:
            # i 의 가장작은 소인수
            p = minFactor[i]

            # 가작 작은 소인수로 나눈 수
            m = i // p

            # i 의 가장작은 소인수와 m 의 가장작은 소인수가 같지 않음
            if p != minFactor[m]:
                minFactorPower[i] = 1

            # i 의 가장작은 소인수와 m 의 가장작은 소인수가 같음
            # i의 가장작은 소인수 = m 의 가장작은 소인수 + 1 승
            else:
                minFactorPower[i] = minFactorPower[m] + 1

            a = minFactorPower[i]

            # m 의 가장작은 소인수의 개수를 대체(+1)하여 기록
            factors[i] = (factors[m]//a) * (a+1)
    return factors

def solution(e, starts):
    factors = getFactorsSmart(e)
    length = len(starts)
    answer = [0] * length
    maxindex = factors.index(max(factors))
    startcopy = []
    for i in range(length):
        startcopy.append([starts[i],i])
    startcopy.sort()
    for i in range(length):
        if startcopy[i][0] > maxindex:
            check = factors[startcopy[i][0]:e+1]
            maxindex = startcopy[i][0]+check.index(max(check))
        answer[startcopy[i][1]] = maxindex
    return answer
