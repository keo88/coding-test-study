def solution(n, m, x, y, r, c, k):
    answer = ''
    kcheck = (k-abs(x-r)-abs(y-c))
    if kcheck%2 != 0 or kcheck < 0:
        return "impossible"
    
    up = down = right = left = 0
    if x-r < 0:
        down = abs(x-r)
    else:
        up = x-r
    if y - c > 0:
        left = y-c
    else:
        right = abs(y-c)
    
    if r == n: 
        left = left + kcheck/2
        right = right + kcheck/2
    else: 
        if kcheck - 2*(n - x) > 0 and x > r:
            down = down + n - x
            up = up + n - x
            kcheck = kcheck - 2*(n - x)
            left = left + kcheck/2
            right = right + kcheck/2
        elif kcheck - 2*(n - r) > 0 :
            down = down + n - r
            up = up + n - r
            kcheck = kcheck - 2*(n - r)
            left = left + kcheck/2
            right = right + kcheck/2
        else:
            down = down + kcheck/2
            up = up + kcheck/2

    for i in range(k):
        if down > 0 and x < n:
            down -= 1
            x += 1
            answer += 'd'
        elif left > 0 and y > 1:
            left -= 1
            y -= 1
            answer += 'l'
        elif right > 0 and y < m:
            right -= 1
            y += 1
            answer += 'r'
        elif up > 0 and x > 1:
            up -= 1
            x -= 1
            answer += 'u'
    return answer
"""dlru"""
