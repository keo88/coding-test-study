def solution(n, computers):
    answer = 0
    bigcor = 0
    bigrelation = []
    while True:
        for i in range(n):
            if sum(computers[i]) > sum(computers[bigcor]):
                bigcor = i
        for i in range(n):
            if computers[bigcor][i] == 1:
                bigrelation.append(i)
        check = True
        while check:
            check = False
            for i in bigrelation:
                for j in range(n):
                    if computers[i][j] == 1 and not(j in bigrelation):
                        bigrelation.append(j)
                        check = True
        answer = answer + 1
        for i in bigrelation:
            computers[i] = [0] * n
        if computers == [[0]*n for i in range(n)]:
            break
        bigcor = 0
        bigrelation = []
    return answer
