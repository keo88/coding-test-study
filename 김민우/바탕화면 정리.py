def solution(wallpaper):
    answer = []
    max_garo = 0
    max_sero = 0
    min_garo = 10000
    min_sero = 10000
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j]=='#'):
                if(max_garo < j+1):
                    max_garo = j+1
                if(min_garo > j):
                    min_garo = j
                if(max_sero < i+1):
                    max_sero = i+1
                if(min_sero > i):
                    min_sero = i

    answer.append(min_sero)
    answer.append(min_garo)
    answer.append(max_sero)
    answer.append(max_garo)
    return answer

print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
