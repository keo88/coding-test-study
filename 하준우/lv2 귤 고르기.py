def solution(k, tangerine):
    answer = 0
    gul = [0]*(max(tangerine)+1)
    for i in range(len(tangerine)):
        gul[tangerine[i]] += 1
    gul.sort(reverse = True)
    for i in range(len(gul)):
        if k < 1:
            break
        k = k - gul[i]
        answer = answer + 1
    return answer
