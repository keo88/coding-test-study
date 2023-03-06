def solution(k, score):
    answer = []
    result = []
    for i in range(len(score)):
        answer.append(score[i])
        answer.sort()
        print(answer)
        if(len(answer)>k):
            answer.pop(0)
        result.append(answer[0])
    return result


print(solution(3,[10, 100, 20, 150, 1, 100, 200]))
