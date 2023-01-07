import math
def solution(my_str, n):
    answer = []
    a = math.ceil(len(my_str)/n)
    for i in range(a):
        answer.append(my_str[i*n:(i+1)*n])
    return answer
