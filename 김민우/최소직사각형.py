def solution(sizes):
    max_garo = 0
    max_sero = 0
    answer = 0

    for i in range(len(sizes)):
        if(sizes[i][0]<sizes[i][1]):
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
        if(max_garo < sizes[i][0]):
            max_garo = sizes[i][0]
        if(max_sero < sizes[i][1]):
            max_sero = sizes[i][1]
    answer = max_garo * max_sero
    
    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
