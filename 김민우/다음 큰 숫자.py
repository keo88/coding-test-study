def solution(n):
    answer = n
    a = bin(n).count('1')
    while True:
        answer += 1
        b = bin(answer).count('1')
        if(a == b):
            break
        
    
    return answer
