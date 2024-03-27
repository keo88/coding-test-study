import sys
from itertools import combinations

int_max = 2**31 - 1

N, M = map(int, sys.stdin.readline().split())
world = list()
for i in range(N):
    world.append(list(sys.stdin.readline().strip().split()))

islands = dict()
init_island = ord('A')
island_count = 0
parents = []


class Island:
    def __init__(self, char, min_x, min_y, max_x, max_y):
        self.char = char
        self.max_x = max_x
        self.min_x = min_x
        self.max_y = max_y
        self.min_y = min_y


def get_islands():
    global island_count

    for i in range(N):
        for j in range(M):
            if world[i][j] == '1':
                min_max_list = color_world(j, i, island_count)
                target_char = chr(init_island + island_count)
                islands[island_count] =  Island(target_char, *min_max_list)
                island_count += 1


def color_world(x: int, y: int, island: int) -> list[int]:
    # min_x, min_y, max_x, max_y
    min_max_lst = [[x, y, x, y]]
    world[y][x] = chr(init_island + island)
    if y + 1 <= N - 1 and world[y + 1][x] == '1':
        min_max_lst.append(color_world(x, y + 1, island))
    if y - 1 >= 0 and world[y - 1][x] == '1':
        min_max_lst.append(color_world(x, y - 1, island))
    if x + 1 <= M - 1 and world[y][x + 1] == '1':
        min_max_lst.append(color_world(x + 1, y, island))
    if x - 1 >= 0 and world[y][x - 1] == '1':
        min_max_lst.append(color_world(x - 1, y, island))
    zipped_list = list(zip(*min_max_lst))
    values = list()
    values.extend(map(min, zipped_list[:2]))
    values.extend(map(max, zipped_list[2:]))
    return values


def build_bridge(from_is: Island, to_is: Island):
    values = []
    is0, is1 = from_is, to_is
    x_range = range(max(is0.min_x, is1.min_x), min(is0.max_x, is1.max_x) + 1)
    y_range = range(max(is0.min_y, is1.min_y), min(is0.max_y, is1.max_y) + 1)

    for x in x_range:
        last_island = '-'
        last_pos = -1
        for k in range(N):
            if world[k][x] != '0':
                found_island = world[k][x]
                if last_island == is0.char or last_island == is1.char:
                    if (found_island == is0.char or found_island == is1.char) and found_island != last_island:
                        bridge_length = k - last_pos - 1
                        if bridge_length >= 2:
                            values.append(bridge_length)

                last_island = found_island
                last_pos = k

    for y in y_range:
        last_island = '-'
        last_pos = -1
        for k in range(M):
            if world[y][k] != '0':
                found_island = world[y][k]
                if last_island == is0.char or last_island == is1.char:
                    if (found_island == is0.char or found_island == is1.char) and found_island != last_island:
                        bridge_length = k - last_pos - 1
                        if bridge_length >= 2:
                            values.append(bridge_length)

                last_island = found_island
                last_pos = k

    if len(values) == 0:
        return int_max
    else:
        return min(values)


bridges = list()


def build_bridges():
    for bridge_tuple in combinations(range(len(islands)), 2):
        bridge_length = build_bridge(islands[bridge_tuple[0]], islands[bridge_tuple[1]])
        bridges.append((*bridge_tuple, bridge_length))


def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def minimum_spanning_tree():
    global parents
    get_islands()
    build_bridges()
    parents = list(range(len(islands)))

    bridges.sort(key=lambda x: x[2])
    answer = 0
    for bridge in bridges:
        if find(bridge[0]) != find(bridge[1]):
            union(bridge[0], bridge[1])
            if bridge[2] == int_max:
                return int_max
            answer += bridge[2]
    return answer


answer = minimum_spanning_tree()
if answer == int_max:
    answer = -1
print(answer)
