def solution(s):
    answer = []
    a = []
    b = 0
    for i in range(len(s)):
        if s[i] not in a:
            answer.append(-1)
            a.append(s[i])

        else:
            for j in range(len(a)):
                if(a[j]==s[i]):
                    big = j

            a.append(s[i])
            answer.append(i-big)

    
    return answer


print(solution("banana"	))
print(solution("footbar"))
