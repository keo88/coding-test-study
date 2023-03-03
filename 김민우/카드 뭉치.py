def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha = [ i for i in alpha if i not in skip]
    print(alpha)
    if(index > len(alpha)):
        index -= len(alpha)
    answer = ''
    for i in s:
        new_idx = alpha.index(i) + index
        if new_idx >= len(alpha):
            new_idx = new_idx -  len(alpha)

        new_i = alpha[new_idx]
        answer += new_i

    return answer

print(solution("aukks","wbqd",5))
