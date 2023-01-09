def solution(elements):
    sumarray = []
    lenelements = len(elements)
    newelements = elements + elements
    for i in range(0, lenelements):
        sumnum = newelements[i]
        for j in range(1,lenelements+1):
            sumthere = False
            sumarray.append(sumnum)
            sumnum = sumnum + newelements[i+j]
    answer = len(set(sumarray))
    return answer
