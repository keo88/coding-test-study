import bisect
import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
candidates = [[]]
keys = [0]


def insert(seq: list, keys: list, data, index: int):
    keys.insert(index, len(data))
    seq.insert(index, data)


def pop(seq: list, keys: list, index: int):
    keys.pop(index)
    seq.pop(index)


def get_len(array: list):
    return len(array)


for i in range(N):
    new_head = arr[i]
    for k in range(len(candidates)):
        candidate = candidates[k]
        if candidate and candidate[-1] >= new_head:
            continue
        new_length = len(candidate) + 1
        cancel = False

        target_index = bisect.bisect_left(keys, new_length)
        for j in range(target_index, len(candidates)):
            if candidates[j][-1] <= new_head:
                cancel = True
                break

        if cancel:
            continue

        new_candidate = candidate + [arr[i]]
        while target_index < len(candidates) and keys[target_index] <= new_length:
            target_index += 1
        insert(candidates, keys, new_candidate, target_index)

        removals = []
        for j in range(1, target_index):
            if candidates[j][-1] >= new_head:
                removals.append(j)

        for removal in removals:
            pop(candidates, keys, removal)

print(keys[-1])
print(' '.join(map(str, candidates[-1])))
