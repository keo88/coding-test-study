import sys


def traverse(node: int, visited: int):
    if visited == visited_all_mask:
        if w[node][start] != 0:
            return w[node][start]
    elif (node, visited) in dp:
        return dp[(node, visited)]

    min_value = int_max
    for city in range(N):
        if (1 << city) & visited == 0 and w[node][city] != 0:
            min_value = min(traverse(city, (1 << city) | visited) + w[node][city], min_value)
    dp[(node, visited)] = min_value

    return min_value


int_max = sys.maxsize
N = int(input())
w = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited_all_mask = (1 << N) - 1
dp = {}
start = 0

print(traverse(start, 1 << 0))
