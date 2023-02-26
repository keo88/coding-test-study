def solution(commands):
    array1 = []
    for i in range(50):
        array = []
        for j in range(50):
            array.append([i,j])
        array1.append(array)
    array2 = [['' for j in range(50)] for i in range(50)]
    
    answer = []
    for k in range(len(commands)):
        command = commands[k].split()
        
        
        if command[0] == 'UPDATE':
            if len(command) == 4:
                array2[array1[int(command[1])-1][int(command[2])-1][0]][array1[int(command[1])-1][int(command[2])-1][1]] = command[3]
            else:
                for i in range(50):
                    for j in range(50):
                        if array2[array1[i][j][0]][array1[i][j][1]] == command[1]:
                            array2[array1[i][j][0]][array1[i][j][1]] = command[2]
                            
                            
        elif command[0] == 'MERGE':
            if (command[1] == command[3] and command[2] == command[4]) or (array1[int(command[3])-1][int(command[4])-1][0] == array1[int(command[1])-1][int(command[2])-1][0] and array1[int(command[3])-1][int(command[4])-1][1] == array1[int(command[1])-1][int(command[2])-1][1]):
                continue
            savenum0 = array1[int(command[3])-1][int(command[4])-1][0]
            savenum1 = array1[int(command[3])-1][int(command[4])-1][1]
            if array2[savenum0][savenum1] != '' and array2[array1[int(command[1])-1][int(command[2])-1][0]][array1[int(command[1])-1][int(command[2])-1][1]] == '':
                array2[array1[int(command[1])-1][int(command[2])-1][0]][array1[int(command[1])-1][int(command[2])-1][1]] = array2[savenum0][savenum1]
            array2[savenum0][savenum1] = ''
            for i in range(50):
                for j in range(50):
                    if array1[i][j][0] == savenum0 and array1[i][j][1] == savenum1:
                        array1[i][j][0] = array1[int(command[1])-1][int(command[2])-1][0]
                        array1[i][j][1] = array1[int(command[1])-1][int(command[2])-1][1]
                        
                        
        elif command[0] == 'UNMERGE':
            savenum0 = array1[int(command[1])-1][int(command[2])-1][0]
            savenum1 = array1[int(command[1])-1][int(command[2])-1][1]
            save1 = array2[savenum0][savenum1]
            for i in range(50):
                for j in range(50):
                    if array1[i][j][0] == savenum0 and array1[i][j][1] == savenum1:
                        array1[i][j][0] = i
                        array1[i][j][1] = j
                        array2[i][j] = ''
            array2[array1[int(command[1])-1][int(command[2])-1][0]][array1[int(command[1])-1][int(command[2])-1][1]] = save1
            
            
        elif command[0] == 'PRINT':
            prin = array2[array1[int(command[1])-1][int(command[2])-1][0]][array1[int(command[1])-1][int(command[2])-1][1]]
            if prin == '':
                answer.append('EMPTY')
            else:
                answer.append(prin)
                
                
    return answer
