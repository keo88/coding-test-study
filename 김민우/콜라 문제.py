def solution(a, b, n):
    answer = 0
    hav = 0
    
    while True:
        d=n%a
        n = (n//a)*b
        answer += n
        n+=d
        if n < a:
            break

    return answer

print(solution(2,1,20))
