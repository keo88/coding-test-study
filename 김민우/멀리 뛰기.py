def solution(n):
    answer1 = 1
    answer2 = 2
    if(n == 1):
        answer = 1
    elif (n == 2):
        answer = 2
    for i in range(2,n):
        answer = answer1 + answer2
        answer1 = answer2
        answer2 = answer
    return answer % 1234567
