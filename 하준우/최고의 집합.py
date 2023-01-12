def solution(n, s):
    if s < n :
        return [-1]
    answer = []
    for i in range(n,1,-1):
        answer.append(s//i)
        s = s - s//i
    answer.append(s)
    answer.sort()
    return answer
