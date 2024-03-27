import sys
import bisect

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
prev_pos = [-1] * len(arr)
keys = [-2**31]
record = [-1]


for i in range(N):
    new_head = arr[i]
    new_pos = bisect.bisect_left(keys, new_head)

    if new_pos == len(keys):
        keys.append(new_head)
        record.append(i)
    else:
        if new_head == keys[new_pos]:
            continue
        else:
            keys[new_pos] = new_head
            record[new_pos] = i
    prev_pos[i] = record[new_pos - 1]

cur_pos, answer = record[-1], [str(arr[record[-1]])]
while prev_pos[cur_pos] != -1:
    cur_pos = prev_pos[cur_pos]
    answer.append(str(arr[cur_pos]))

print(len(keys) - 1)
print(' '.join(reversed(answer)))
