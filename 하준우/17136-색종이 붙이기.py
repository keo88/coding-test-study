import copy
import sys


def countarray(array):
    countnum = 0
    for sero in range(0,10):
        for garo in range(0,10):
            if array[sero][garo] == 1:
                countnum = countnum + 1
    return countnum


def check(sero,garo,seroiter,garoiter,size,array):
    if array[sero+(size-1)*seroiter][garo] == 1 and array[sero][garo+(size-1)*garoiter] == 1 and array[sero+(size-1)*seroiter][garo+(size-1)*garoiter] == 1:
        for checksero in range(sero, sero+(size)*seroiter, seroiter):
            for checkgaro in range(garo, garo+(size)*garoiter, garoiter):
                if array[checksero][checkgaro] == 0:
                    return False
        return True
    else:
        return False


def find(size,seroiter,garoiter,array):
    for sero in range(((9)-(9)*seroiter)//2, ((9)-(9)*seroiter)//2+(11-size)*seroiter, seroiter):
        for garo in range(((9)-(9)*garoiter)//2, ((9)-(9)*garoiter)//2+(11-size)*garoiter, garoiter):
            if array[sero][garo] == 1:
                if check(sero,garo,seroiter,garoiter,size,array):
                    return True
    return False



def clear(size,seroiter,garoiter,array,bullet):
    num = 0
    for sero in range(((9)-(9)*seroiter)//2, ((9)-(9)*seroiter)//2+(11-size)*seroiter, seroiter):
        for garo in range(((9)-(9)*garoiter)//2, ((9)-(9)*garoiter)//2+(11-size)*garoiter, garoiter):
            if array[sero][garo] == 1 and bullet[size - 1] != 0 and check(sero,garo,seroiter,garoiter,size,array):
                array = cleararray(sero,garo,seroiter,garoiter,size,copy.deepcopy(array))
                num = num + 1
                bullet[size - 1] = bullet[size - 1] -1
    return array, num, bullet



def uniclear(size,seroiter,garoiter,array,bullet):
    num = 0
    getout = False
    array
    for sero in range(((9)-(9)*seroiter)//2, ((9)-(9)*seroiter)//2+(11-size)*seroiter, seroiter):
        if getout:
            break
        for garo in range(((9)-(9)*garoiter)//2, ((9)-(9)*garoiter)//2+(11-size)*garoiter, garoiter):
            if array[sero][garo] == 1 and bullet[size - 1] != 0 and check(sero,garo,seroiter,garoiter,size,array):
                arrayresult = cleararray(sero,garo,seroiter,garoiter,size,array)
                num = num + 1
                bullet[size - 1] = bullet[size - 1] -1
                getout = True
                break
    return arrayresult, num, bullet
            



def cleararray(sero,garo,seroiter,garoiter,size,array):
    for checksero in range(sero, sero+size*seroiter, seroiter):
        for checkgaro in range(garo, garo+size*garoiter, garoiter):
            array[checksero][checkgaro] = 0
    return array



def solve(size,array,bullet,num):
    
    if size == 1:
        arraycopy, numget, bulletcopy = clear(1,1,1,array,bullet)
        return num + numget

    elif size == 2:
        arraycopy, numget, bulletcopy = clear(2,1,1,copy.deepcopy(array),copy.deepcopy(bullet))
        if countarray(arraycopy) > 5:
            return 99
        return solve(1, arraycopy, bulletcopy, num + numget)

    else:
        if size == 3 and bullet[2]==5 :
            if countarray(array)>65:
                return 99
        if size == 4 and bullet[3]==5:
            if countarray(array)>85:
                return 99
        if not find(size,1,1,array):
            return solve(size-1,copy.deepcopy(array),copy.deepcopy(bullet),num)
        elif bullet[size-1] == 0:
            return solve(size-1,copy.deepcopy(array),copy.deepcopy(bullet),num)
        else:
            small = solve(size-1,copy.deepcopy(array),copy.deepcopy(bullet),num)
            for i,j in [[1,1],[1,-1],[-1,1],[-1,-1]]:
                arraycopy, numget, bulletcopy = uniclear(size,i,j,copy.deepcopy(array),copy.deepcopy(bullet))
                newnum = numget + solve(size,arraycopy,bulletcopy,num)
                if newnum < small:
                    small = newnum
            return small


world = []

for i in range(10):
    row = list(map(int, sys.stdin.readline().split()))
    world.append(row)
answer = solve(5,world,[5,5,5,5,5],0)

if answer > 90:
    answer = -1
    
print(answer)
                    
