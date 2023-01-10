def solution(n):
    answer = 0
    a = 0
    k = 0
    m = len(n)
    nums = []
    for i in range(0,m):
        a = 0
        nums.append([])
        for j in range(0,m):
            k = i + j    
            if(k>=m):
                k = k-m
            a = a + n[k]
            nums.append(a)

    nums.sort()
    result1 = set(nums)
    result2 = list(result1)
    answer = len(result2)
    return answer
