def solution(s, skip, index):
    answer = ''
    for i in range(len(s)):
        num = ord(s[i])
        for j in range(index):
            if num == 122:
                num = num - 26
            num += 1
            while chr(num) in skip:
                if num == 122:
                    num = num - 26
                num += 1
        answer += chr(num)
    return answer
