def check(s):
    a, b, c = 0, 0 ,0
    for i in range(len(s)):
        if(s[i]=='{'):
            a += 1
        if(s[i]=='['):
            b += 1
        if(s[i]=='('):
            c += 1
        if(s[i]=='}'):
            a -= 1
        if(s[i]==']'):
            b -= 1
        if(s[i]==')'):
            c -= 1
        if (a < 0 or b < 0 or c < 0):
            return False
            break
    if(a == 0 and b == 0 and c == 0):
        return True    
    else:
        return False
        
    
def solution(s):     
    answer = 0
    for i in range(len(s)):
        s = s[1:]+s[0]
        print(s)
        if(check(s)):
            answer+=1
    return answer

print(solution("[{]}"))
print(solution(	"[](){}"))
