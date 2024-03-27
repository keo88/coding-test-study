def solution(plans):
    answer = []

    tasks = []
    for p in plans:
        hour, minute = map(int, p[1].split(':'))
        tasks.append([hour * 60 + minute, int(p[2]), p[0]])
    tasks.sort(key=lambda x: x[0])

    stack = []
    lastTime = 0
    for task in tasks:
        curTime = task[0]
        timeDiff = curTime - lastTime
        while timeDiff > 0 and stack:
            timeLeft = stack[-1][1]
            if timeLeft <= timeDiff:
                timeDiff -= timeLeft
                answer.append(stack.pop()[2])
            else:
                stack[-1][1] -= timeDiff
                timeDiff = 0
        stack.append(task)
        lastTime = curTime

    while stack:
        answer.append(stack.pop()[2])

    return answer