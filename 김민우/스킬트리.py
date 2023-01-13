def solution(skill, skill_trees):
    answer = 0
    
    for i in range(len(skill_trees)):
        index = 0
        a = 0
        for j in range(len(skill_trees[i])):
            if(skill_trees[i][j] in skill):
                if(skill_trees[i][j] == skill[index]):
                    index += 1
                else:
                    a += 1
        if (a == 0):        
            answer += 1
        
            
    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])

