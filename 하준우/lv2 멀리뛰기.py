import math
def solution(n):
    answer = 0
    full2 = n//2
    for i in range(full2+n%2,n+1):
        answer = answer + math.comb(i,full2)
        full2 = full2 - 1
    return answer%1234567
