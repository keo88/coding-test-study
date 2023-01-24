def solution(n):
    ans = 1
    
    while True:
        if(n==1):
            break
        else:
            if(n%2 ==1 ):
                ans += 1
            n = n//2

    return ans

print(solution(5000))
