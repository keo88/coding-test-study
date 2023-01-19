def solution(genres, plays):
    answer = []
    genremoum = list(set(genres))
    newarray = []
    
    for i in range(len(genremoum)):
        newarray.append([])
        
    for i in genremoum:
        for j in range(len(genres)):
            if genres[j]==i:
                newarray[genremoum.index(i)].append([i,plays[j],j])
        newarray[genremoum.index(i)].sort(key=lambda x:-x[1])
                
    for i in range(len(genremoum)):
        numplay = 0
        for j in range(len(newarray[i])):
            numplay = numplay + newarray[i][j][1]
        genremoum[i] = [genremoum[i],numplay]
    
    for i in range(len(genremoum)):
        albumorder = -1
        genreplay = 0
        for j in range(len(genremoum)):
            if genremoum[j][1] > genreplay:
                genreplay = genremoum[j][1]
                albumorder = j
        genremoum[albumorder][1] = 0
        if len(newarray[albumorder]) == 1:
             answer.append(newarray[albumorder][0][2])
        else:
            for j in range(0,2):
                answer.append(newarray[albumorder][j][2])
    
    return answer
