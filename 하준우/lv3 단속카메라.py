def solution(routes):
    answer = 0
    routes.sort()
    while len(routes) != 0:
        if len(routes) == 1:
            routes.pop(0)
        else:
            pole = 1
            start = routes[0][0]
            end = routes[0][1]
            for i in range(1,len(routes)):
                if start <= routes[i][0] and routes[i][0] <= end:
                    pole = pole + 1
                    start = routes[i][0]
                    end = min(end,routes[i][1])
                else:
                    break
            for i in range(pole):
                routes.pop(0)
        answer = answer + 1
    return answer

"""
def solution(routes):
    answer = 0
    routes.sort()
    while len(routes) != 0:
        if len(routes) == 1:
            routes.pop(0)
        elif routes[0][1] < routes[1][0]:
            routes.pop(0)
        else:
            checkpole = 0
            for i in range(routes[1][0],routes[0][1]+1):
                newpole = 0
                for j in range(len(routes)):
                    if routes[j][0] <= i and i <= routes[j][1]:
                        newpole = newpole + 1
                if checkpole <= newpole:
                    checkpole = newpole
                else:
                    break
            for i in range(checkpole):
                routes.pop(0)
        answer = answer + 1
    return answer
"""
