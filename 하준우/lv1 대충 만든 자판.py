def solution(keymap, targets):
    answer = [0] * len(targets)
    key = {}
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] in key:
                if key[keymap[i][j]] > j+1:
                    key[keymap[i][j]] = j+1
            else:
                key[keymap[i][j]] = j+1
    for i in range(len(targets)):
        for j in range(len(targets[i])):
            if targets[i][j] in key:
                answer[i] += key[targets[i][j]]
            else:
                answer[i] = -1
                break
    return answer
