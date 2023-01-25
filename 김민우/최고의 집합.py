def solution(n, s):
    answer = []
    avr = 0
    rem = 0
    if(n>s):
        answer.append(-1)
        return answer
    avr = s//n
    rem = s%n
    for i in range(0,n):
        answer.append(avr)
    for j in range(0,n):
        if rem == 0:
            break
        answer[j] += 1
        rem -= 1
    answer.reverse()
    return answer
