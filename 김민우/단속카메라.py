def solution(routes):
    answer = 0
    point = -30001
    routes.sort(key=lambda x:x[1])


    for i in range(len(routes)):
        if(routes[i][0] > point and routes[i][1] > point):
            point  = routes[i][1]
            answer += 1 
    
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))#2
print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-2], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
