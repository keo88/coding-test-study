def solution(s):
    answer = ''
    dick = {}
    for i in range(len(s)):
        if s[i] in dick:
            dick[s[i]] += 1
        else:
            dick[s[i]] = 1
    bae = []
    for i in range(len(s)):
        if dick[s[i]] == 1:
            bae.append(s[i])
    bae.sort()
    for i in range(len(bae)):
        answer += bae[i]
    return answer
