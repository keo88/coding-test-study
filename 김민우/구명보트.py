def solution(people, limit):
    answer = 0
    people.sort()
    
    while (people != []):
        a = people.pop()
        if(people == []):
            answer += 1
            break
        elif(a + people[0]<= limit):
            people.pop(0)
            answer += 1
        else:
            answer += 1

    print(answer)
   
    return answer


solution([70, 80, 50], 100)
