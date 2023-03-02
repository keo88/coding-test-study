def solution(price, money, count):
    a = 0
    for i in range(1,count+1):
        a += i*price
        print(a)
    answer = money - a
    if(answer > 0):
        return 0
    else:
        return answer*(-1)

print(solution(3,20,4))
