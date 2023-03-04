def solution(today, terms, privacies):
    answer = []
    today = list(map(int,today.split('.')))
    print(today)
    
    for i in range(len(terms)):
        alpha, month = terms[i].split(' ')
        print(alpha, month)
        for j in range(len(privacies)):
            if(alpha==privacies[j][-1]):
                privacies[j] = privacies[j][:-2]
                privacies[j] = list(map(int,privacies[j].split('.')))
                privacies[j][1] += int(month)
                while(privacies[j][1] > 12):
                    privacies[j][1] -= 12
                    privacies[j][0] += 1
                print(privacies[j])
                if(privacies[j][0] < today[0]):
                    answer.append(j+1)
                if(privacies[j][0] == today[0] and privacies[j][1] < today[1]):
                    answer.append(j+1)
                if(privacies[j][0] == today[0] and privacies[j][1] == today[1] and privacies[j][2] <= today[2]):
                    answer.append(j+1)
    answer.sort()
    return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
