def getMyDivisor(n):
    count = 0

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0) :
            count += 1
            if(i **2 != n):
                count += 1
            
    return count


def solution(number, limit, power):
    a = 0
    answer = 0
    for j in range(1,number+1):
        a = getMyDivisor(j)
        if(a>limit):
            a = power
        answer += a

        
    return answer


print(solution(5,3,2))
