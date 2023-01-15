def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    anum = 0
    for i in range(len(A)):
        if B[i] > A[anum]:
            answer = answer + 1
            anum = anum + 1
    return answer
