import sys


def dfs(cur_node: int, acc: int):
    values = []
    visited.append(cur_node)
    for edge, length in E[cur_node - 1]:
        if edge not in visited:
            values.append(dfs(edge, acc + length))
    if len(values) == 0:
        answer = acc, cur_node
    else:
        cur_max, cur_max_node = -1, -1
        for i in range(len(values)):
            if values[i][0] > cur_max:
                cur_max = values[i][0]
                cur_max_node = values[i][1]
        answer = cur_max, cur_max_node

    visited.pop()
    return answer


V = int(input())
E = {}
visited, max_value = [], -1
for i in range(V):
    line = list(map(int, sys.stdin.readline().split()))
    E[line[0] - 1] = list()
    for j in range(1, len(line) - 1, 2):
        E[line[0] - 1].append((line[j], line[j + 1]))

_, first_max_node = dfs(1, 0)
max_value, second_max_node = dfs(first_max_node, 0)
print(max_value)
