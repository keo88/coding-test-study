def solution(s):
    count = 0
    count2 = 0
    while s != "1":
        count += s.count("0")
        s = bin(s.count("1"))[2:]
        count2 += 1
    return [count2, count]

print(solution("110010101001"))
