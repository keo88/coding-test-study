def solution(numbers):
    keys = []
    for n in numbers:
        sn = str(n)
        if len(sn) == 1:
            keys.append((f'{sn}{sn}{sn}{sn}', sn))
        elif len(sn) == 2:
            keys.append((f'{sn}{sn[0]}{sn[1]}', sn))
        elif len(sn) == 3:
            keys.append((f'{sn}{sn[0]}', sn))
        else:
            keys.append((sn, sn))
    sortedKeys = list(reversed(sorted(keys)))
    if sortedKeys[0][1] == '0':
        return '0'
    return ''.join(map(lambda s: s[1], sortedKeys))