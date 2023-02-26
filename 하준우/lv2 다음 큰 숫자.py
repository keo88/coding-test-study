def solution(n):
    count = bin(n).count('1')
    while True:
        n += 1
        if bin(n).count('1') == count:
            return n
