def solution(n,a,b):
    answer = 0
    count = 0
    s = n
    temp1 = 0
    temp2 = n
    mid = n//2
    while True:
        s//=2
        count += 1
        if s == 1:
            break
    if(a>b):
        a, b = b, a
    while True:
        if(a<=mid and b>mid):
            print('힝')
            break
        if(a<=mid and b<=mid):
            temp2 = mid
            mid = (temp1 + mid) //2
            count -= 1
            print('잉')
            if mid == 1:
                break
        if(a>mid and b>mid):
            temp1 = mid
            mid = (mid+temp2)//2
            count -= 1
            print('삥')
            if mid == n-1:
                break
    answer = count


    return answer

print(solution(16,9,12))
