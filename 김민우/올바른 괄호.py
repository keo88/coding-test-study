def solution(s):
    answer = True
    count = 0
    d = len(s)
    for i in range(0,d):
        if(count < 0):
            return False
        if(s[i]==")"):
            count -= 1
        if(s[i]=="("):
            count += 1
            
    if(count == 0):
        answer = True
    else:
        answer = False
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer
