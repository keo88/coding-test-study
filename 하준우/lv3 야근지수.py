def solution(n, works):
    answer = 0

    works.sort()
    works = [i for i in works if i not in {0}]

    while works[-1] != 0 and n != 0:
        maxcount = works.count(works[-1])
        if maxcount == 1:
            works[-1] = works[-1] - 1
            n = n-1
        elif not n < maxcount:
            for i in range(maxcount):
                works[-1-i] = works[-1-i] - 1
                n = n-1
        else:
            for i in range(n):
                works[-1-i] = works[-1-i] - 1
                n = n-1

    for i in range(len(works)):
        answer = answer + works[i] * works[i]

    return answer
