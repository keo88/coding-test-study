def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i]//2 >= 1:
            for j in range(food[i]//2):
                answer += str(i)
    answer2 = answer[::-2]        
    answer += '0'
    answer += answer2
    
    
    return answer

print(solution([1, 7, 1, 2]))
