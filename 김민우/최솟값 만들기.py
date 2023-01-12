def solution(A,B):
    answer = 0
    arr = []
    A.sort()
    B.sort()
    B.reverse()
    a = A
    b = B
    for i in range(0,len(a)):
        arr.append([])
        arr[i] = a[i]*b[i]
    answer = sum(arr)
    print(answer)
    return answer

solution([1,2],[3,4])
