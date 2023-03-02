def solution(s):
    answer = 0
    word_list=['zero','one','two','three','four','five','six','seven','eight','nine']
    num_list=[0,1,2,3,4,5,6,7,8,9]
    for word, i in zip(word_list,num_list):
        s=s.replace(word,str(i))
    answer=int(s)  
    return answer
