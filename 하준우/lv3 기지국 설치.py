def solution(n, stations, w):
    answer = 0
    check = 1
    stacheck = 0
    if check + w < stations[stacheck]:
        check = check + w
        answer = answer + 1
    else:
        check = stations[stacheck]
        stacheck = stacheck + 1
    while check < n - w :
        if stacheck > len(stations) - 1:
            check = check + 2*w + 1
            answer = answer + 1
        elif check + 2*w +1 < stations[stacheck]:
            check = check + 2*w + 1
            answer = answer + 1
        elif check + 2*w +1 >= stations[stacheck]:
            check = stations[stacheck]
            stacheck = stacheck + 1
    return answer
