import sys

N = 10
cap = 5
maximum_int = 2**31 - 1

init_world = []
maximum_area = [0, 5, 25, 70, 89]

init_ones = 0
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    init_world.append(row)
    init_ones += sum(row)

global_best_value = maximum_int


def duplicate_grid(world: list[list]):
    new_world = []
    for row in world:
        new_world.append(row.copy())
    return new_world


def get_candidates(world: list[list], s: int):
    candidates = []

    for y in range(s - 1, N):
        for x in range(s - 1, N):

            all_1 = True
            for i in range(y - s + 1, y + 1):
                if all_1:
                    for j in range(x - s + 1, x + 1):
                        if world[i][j] != 1:
                            all_1 = False
                            break

            if all_1:
                candidates.append((x, y))
    return candidates


def get_node_value(world: list[list[int]], acc_points: set[(int, int)], left_ones: int, s: int):
    global global_best_value

    if s == 0 or (left_ones // s**2) + len(acc_points) >= global_best_value:
        return world, acc_points, maximum_int
    candidates = get_candidates(world, s)
    paths = get_paths(world, left_ones, set(), candidates, s)

    best_world = []
    best_points = []
    for new_world, area_left, new_points in reversed(paths):
        new_acc_points = acc_points.union(new_points)
        value = len(new_acc_points)

        if value >= global_best_value:
            continue

        if area_left > 0:
            new_world, new_acc_points, value = get_node_value(new_world, new_acc_points, area_left, s - 1)
        if value < global_best_value:
            global_best_value = value
            best_points = new_acc_points
            best_world = new_world

    return best_world, best_points, global_best_value


def get_paths(world: list[list], area: int, points: set[int], candidates: list[(int, int)], s: int) -> list[(list[list[int]], list[(int, int)])]:

    points_array = [(world, area, points)] if maximum_area[s - 1] >= area else []

    if len(candidates) == 0 or len(points) == 5:
        return points_array

    for candidate in candidates:
        new_points = points.copy()
        main_point = candidate
        new_points.add(main_point)
        new_world = duplicate_grid(world)
        left_ones = area - s ** 2

        for y in range(main_point[1] - s + 1, main_point[1] + 1):
            for x in range(main_point[0] - s + 1, main_point[0] + 1):
                new_world[y][x] = s

        new_candidates = candidates.copy()
        for i in range(len(candidates)):
            if abs(candidates[i][1] - main_point[1]) < s and abs(candidates[i][0] - main_point[0]) < s:
                new_candidates.remove(candidates[i])
        points_array.extend(get_paths(new_world, left_ones, new_points, new_candidates, s))

    return points_array


world, points, answer = get_node_value(init_world, set(), init_ones, 5)
if answer == maximum_int:
    answer = -1
print(answer)
