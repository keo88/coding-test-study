def solution(n):

    count = 0
    for i in range(0,n):
        a = i
        sum = 0
        for j in range(0,n):
            a += 1
            sum += a
            if (sum == n):
                count += 1
                break
            elif(sum > n):
                break
    return count
