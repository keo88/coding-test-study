import sys
from heapq import heappush, heappop, heapify
from collections import deque

intMax = 2 **31 -1
Q = int(input())
_, Nstr, u0 = sys.stdin.readline().split()
N = int(Nstr)


def getDomain(s: str):
    return s.split('/')[0]


du0 = getDomain(u0)
# wDeque = { du0: {
#   pr: deque([])
# }}
# wUrlSet = {u0}
# wPriorityList = {du0: [1]}

wDeque: dict[str, dict[int, deque]] = {}
wUrlSet = set()
wPriorityList: dict[str, list[int]] = {}
tot = 0


def add_wait(u, pr, ti):
    if u in wUrlSet:
        return
    global tot
    tot += 1
    du = getDomain(u)

    if not du in wDeque:
        wDeque[du] = {}
    if not pr in wDeque[du]:
        wDeque[du][pr] = deque([])

    if not du in wPriorityList:
        wPriorityList[du] = []

    heappush(wPriorityList[du], pr)
    wDeque[du][pr].append((ti, u))
    wUrlSet.add(u)


def remove_wait(exclude_du: list[str]):
    best_key, best_pr, best_ti = None, intMax, intMax

    for key in wPriorityList:
        if key in exclude_du:
            continue
        front_pr = wPriorityList[key][0]
        if front_pr < best_pr:
            front_ti = wDeque[key][front_pr][0][0]
            best_pr = front_pr
            best_ti = front_ti
            best_key = key
        elif front_pr == best_pr:
            front_ti = wDeque[key][front_pr][0][0]
            if front_ti < best_ti:
                best_ti = front_ti
                best_key = key

    if not best_key:
        return

    global tot
    tot -= 1
    heappop(wPriorityList[best_key]) # best_pr
    if not wPriorityList[best_key]:
        del wPriorityList[best_key]
    _, best_url = wDeque[best_key][best_pr].popleft() # best_ti
    if not wDeque[best_key][best_pr]:
        del wDeque[best_key][best_pr]
        if not wDeque[best_key]:
            del wDeque[best_key]
    wUrlSet.remove(best_url)

    return best_key, best_pr, best_ti


add_wait(u0, 1, 0)

dus: dict[str, tuple[int, int]] = {}
judge = list(range(1, N + 1))
heapify(judge)
workingJudge = {}

for i in range(Q - 1):
    command = list(sys.stdin.readline().split())
    typ = int(command[0])
    if typ == 200:
        tstr, pstr, u = command[1:]
        t, p = int(tstr), int(pstr)
        add_wait(u, p, t)
    elif typ == 300:
        if len(judge) == 0:
            continue

        t = int(command[1])
        filter_dus = []
        for du in dus:
            start_t, end_t = dus[du]
            if t < end_t:
                filter_dus.append(du)
        res = remove_wait(filter_dus)
        if res:
            du, pr, start_t = res
            dus[du] = (t, intMax)
            j = heappop(judge)
            workingJudge[j] = (t, du)
    elif typ == 400:
        t, jId = map(int, command[1:])
        if jId in workingJudge:
            start_t, du = workingJudge[jId]
            del workingJudge[jId]
            heappush(judge, jId)
            gap = t - start_t
            end_t = start_t + 3 * gap
            dus[du] = (start_t, end_t)
    elif typ == 500:
        print(tot)
