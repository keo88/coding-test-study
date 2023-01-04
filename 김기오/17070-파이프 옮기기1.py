import sys

N = int(sys.stdin.readline())
room = [[]] * N
cur_pos = 0, 1
init_dir = 0
mem = dict()


def addTuple(tup1: (int, int), tup2: (int, int)):
    return tup1[0] + tup2[0], tup1[1] + tup2[1]


def getRoomValue(pos: (int, int)):
    global room
    return room[pos[0]][pos[1]]


def countWays(direction: int, pos: (int, int), dest: (int, int)):
    if pos == dest:
        return 1
    elif (pos, direction) in mem:
        return mem[pos, direction]

    is_right_empty = True if (pos[1] < N - 1) and getRoomValue(addTuple(pos, (0, 1))) == 0 else False
    is_down_empty = True if (pos[0] < N - 1) and getRoomValue(addTuple(pos, (1, 0))) == 0 else False
    is_diag_empty = True if is_right_empty and is_down_empty and getRoomValue(addTuple(pos, (1, 1))) == 0 else False

    answer = 0

    if (direction == 0 or direction == 1) and is_right_empty:
        answer += countWays(0, addTuple(pos, (0, 1)), dest)
    if is_diag_empty:
        answer += countWays(1, addTuple(pos, (1, 1)), dest)
    if (direction == 1 or direction == 2) and is_down_empty:
        answer += countWays(2, addTuple(pos, (1, 0)), dest)

    mem[pos, direction] = answer
    return answer


for i in range(N):
    room[i] = list(map(lambda x: int(x), sys.stdin.readline().strip().split(sep=' ')))

print(countWays(init_dir, cur_pos, (N - 1, N - 1)))
