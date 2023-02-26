def solution(n):
    answer = 1
    for i in range(1,(n+1)//2):
        math = 0
        while math <= n:
            if math == n:
                answer += 1
            math += i
            i += 1
    return answer
