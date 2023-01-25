def solution(n, words):
    arr = []
    answer = []
    arr.append(words[0])

    for i in range(1,len(words)):
        arr.append(words[i])
        if(words[i-1][-1]!=words[i][0]):
            answer = [(i%n)+1,(i//n)+1]
            break
        if(arr.count(words[i])>1):         
            answer = [(i%n)+1,(i//n)+1]
            break
        else:
            answer = [0,0]
    
    print(answer)
    return answer

solution(3  , ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
solution(2, ["land", "dream", "mom", "mom", "ror"])
