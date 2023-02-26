def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    for i in range(n-1, -1, -1):
        for j in range(i-1,-1,-1):
            if numbers[i] <= numbers[j]:
                break
            answer[j] = numbers[i]
    return answer
