def solution(ingredient):
    s = []
    answer = 0
    for i in ingredient:
        s.append(i)
        while s[-4:] == [1, 2, 3, 1]:
            s.pop()
            s.pop()
            s.pop()
            s.pop()
            answer += 1

    return answer
