def solution(operations):
    answer = []
    arr = []
    for i in range(len(operations)):
        if(operations[i]=="D 1"):
            if(arr != []):
                del arr[0]

        elif(operations[i]=="D -1"):
            if(arr != []):
                del arr[-1]

        else:
            arr.append(operations[i][2:])
            arr.sort(reverse = True, key = int)

            

    if(arr == []):
        answer = [0,0]
    else:
        answer = [int(arr[0]),int(arr[-1])]
        print(answer)

    
    
    return answer

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])
