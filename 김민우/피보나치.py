def solution(n):
    answer = 0
    a,b = 0, 1
    for i in range(0,n):
        temp = a
        a = b
        b = temp + a
    
    answer = a
    return answer%1234567
