def solution(triangle):
    for i in range(len(triangle)-2,-1,-1):
        for j in range(0,len(triangle[i])):
            triangle[i][j] = triangle[i][j] + max(triangle[i+1][j],triangle[i+1][j+1])
    return triangle[0][0]

"""
탑다운

def trianglesum(array,nowcol,nowrow,num):
    if nowrow == len(array)-1:
        return num + array[nowrow][nowcol]
    else:
        return max(trianglesum(array,nowcol,nowrow+1,num+array[nowrow][nowcol]),trianglesum(array,nowcol+1,nowrow+1,num+array[nowrow][nowcol]))

def solution(triangle):
    return trianglesum(triangle,0,0,0)

================================================================================

다운탑

def trianglesum(array,nowrow,nowcol,num):
    if nowrow == 0:
        return num+array[nowrow][nowcol]
    elif nowcol == 0:
        return trianglesum(array,nowrow-1,nowcol,num+array[nowrow][nowcol])
    elif nowcol == len(array[nowrow])-1:
        return trianglesum(array,nowrow-1,nowcol-1,num+array[nowrow][nowcol])
    else:
        return max(trianglesum(array,nowrow-1,nowcol-1,num+array[nowrow][nowcol]),trianglesum(array,nowrow-1,nowcol,num+array[nowrow][nowcol]))

def solution(triangle):
    answer = -1
    for i in range(0,len(triangle[len(triangle)-1])):
        check = trianglesum(triangle,len(triangle[len(triangle)-1])-1,i,0)
        if answer < check:
            answer = check
    return answer

"""
