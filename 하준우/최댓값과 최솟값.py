def solution(s):
    answer = s.split(' ')
    for i in range(0,len(answer)):
        answer[i] = int(answer[i])
    answer.sort()
    return "".join([str(answer[0]),' ',str(answer[len(answer)-1])])

