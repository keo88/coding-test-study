import sys
sys.setrecursionlimit(10**6)

def dist(start,end,phone):
    sero = abs(phone[start][0] - phone[end][0])
    garo = abs(phone[start][1] - phone[end][1])
    if sero == 0 and garo == 0:
        return 1
    else:
        return 2*(sero+garo) - min(sero,garo)
    
def create(left,right,now,end,phone,numbers,dick):
    key = str(left)+str(right)+str(now)
    get = int(numbers[now])
    if left == right:
        return 9999999999999999
    if key in dick:
        return dick[key]
    if now == end-1:
        dick[key] = min(dist(right,get,phone),dist(left,get,phone))
        return dick[key]
    else:
        dick[key] = min(create(get,right,now+1,end,phone,numbers,dick)+dist(left,get,phone),create(left,get,now+1,end,phone,numbers,dick)+dist(right,get,phone))
        return dick[key]

def solution(numbers):
    answer = 0
    dick = {}
    left, right = 4,6
    end = len(numbers)
    phone = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    return create(left,right,0,end,phone,numbers,dick)

"""
def dist(start,end,phone):
    sero = abs(phone[start][0] - phone[end][0])
    garo = abs(phone[start][1] - phone[end][1])
    if sero == 0 and garo == 0:
        return 1
    else:
        return 2*(sero+garo) - min(sero,garo)

def check(left,right,now,end,time,phone,numbers):
    if now >= end:
        return time
    get = int(numbers[now])
    if dist(left,get,phone) == dist(right,get,phone):
        return min(check(get,right,now+1,end,time+dist(left,get,phone),phone,numbers),check(left,get,now+1,end,time+dist(right,get,phone),phone,numbers))
    if dist(left,get,phone) < dist(right,get,phone):
        return check(get,right,now+1,end,time+dist(left,get,phone),phone,numbers)
    else:
        return check(left,get,now+1,end,time+dist(right,get,phone),phone,numbers)

def solution(numbers):
    left, right = 4,6
    end = len(numbers)
    phone = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    return check(left,right,0,end,0,phone,numbers)


def dist(start,end,phone):
    sero = abs(phone[start][0] - phone[end][0])
    garo = abs(phone[start][1] - phone[end][1])
    if sero == 0 and garo == 0:
        return 1
    else:
        return 2*(sero+garo) - min(sero,garo)

def solution(numbers):
    answer = 0
    left, right = 4,6
    end = len(numbers)
    phone = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    for i in range(end):
        get = int(numbers[i])
        if dist(left,get,phone) <= dist(right,get,phone):
            answer += dist(left,get,phone)
            left = get
        else:
            answer += dist(right,get,phone)
            right = get
    return answer
"""
