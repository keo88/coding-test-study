def solution(t, p):
    answer = 0
    for i in range(0,len(t)-len(p)+1):
        x = t[i:len(p)+i]
        if(x<=p):
            answer+=1
    return answer


print(solution("3141592","271"))
print(solution("500220839878","7"))
