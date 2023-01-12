def solution(s):
    answer = ''
    a = s.lower().split(' ')
    for i in range(0,len(a)):
        a[i] = a[i].capitalize()

    answer = " ".join(a)
    print(answer)  
    return answer

solution("3people unFollowed me")
