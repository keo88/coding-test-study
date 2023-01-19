def solution(s):
    arr = []
    answer = -1
    
    for i in s:
        arr.append(i)
        if(len(arr)>1):
            if(arr[-1]==arr[-2]):
                arr.pop()
                arr.pop()
    if arr == []:
        answer = 1
    else:
        answer = 0
        
    return answer
print(solution("baabaa"))
