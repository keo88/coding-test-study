def solution(n):
    tri = ''
    while(n):
        if(n%3 != 0):
            a = n%3
        else:
            a = 3
            n -= 3
        tri += str(a)
        n = n//3
    answer = tri[::-1]
    answer = answer.replace("3","4")
    return answer
