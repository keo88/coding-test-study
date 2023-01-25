def solution(scores):
    for i in range(len(scores)):
        if scores[0][0] < scores[i][0] and scores[0][1] < scores[i][1]:
            return -1
    array = []
    for i in range(len(scores)):
        array.append([scores[i][0]+scores[i][1],i,scores[i][0],scores[i][1]])
    array.sort(reverse = True)
    big = [0,0]
    big0 = [0,0]
    big1 = [0,0]
    for i in range(len(scores)-1,-1,-1):
        if array[i][2] > big[0] and array[i][3] > big[1]:
            big[0] = array[i][2]
            big[1] = array[i][3]
        if array[i][2] > big0[0]:
            big0[0] = array[i][2]
            big0[1] = array[i][3]
        if array[i][3] > big1[1]:
            big1[0] = array[i][2]
            big1[1] = array[i][3]
    for i in range(len(array)):
        if (array[i][2] < big[0] and array[i][3] < big[1]) or (array[i][2] < big0[0] and array[i][3] < big0[1]) or (array[i][2] < big1[0] and array[i][3] < big1[1]):
            array[i][0] = 0
    array.sort(reverse = True)
    rank = array.index([scores[0][0]+scores[0][1],0,scores[0][0],scores[0][1]]) + 1
    same = 0
    for i in range(array.index([scores[0][0]+scores[0][1],0,scores[0][0],scores[0][1]])):
        if array[i][0] == scores[0][0]+scores[0][1]:
            same = same + 1
            continue
        if array[i][2] == big0[0] or array[i][3] == big1[1]:
            continue
        for j in range(0,i):
            if array[j][2] > array[i][2] and array[j][3] > array[i][3]:
                same = same + 1
                break
    return rank - same
