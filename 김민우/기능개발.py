import math

def solution(progresses, speeds):
    answer = []
    done = math.floor((100-progresses[0])/speeds[0])
    day = 0
    count = 1
    for i in range(0, len(progresses)):
        day = math.ceil((100-progresses[i])/speeds[i])
        print(day)
        if(done > day):
            done = day
            answer.append(count)
            count = 1
        if(done <= day):
            count += 1
            print(str(count))


    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))

