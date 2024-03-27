import sys


def dfs(lst: list, last_int: int, max_int: int) -> int:
    results = [calc(lst)]
    for i in range(last_int + 2, max_int):
        new_lst = lst.copy()
        new_lst.append(i)
        results.append(dfs(new_lst, i, max_int))

    return max(results)


def calc(order: list):
    full_order = order.copy()
    calc_ints = ints.copy()
    calc_ops = ops.copy()
    rng = list(range(op_cnt))
    for j in order:
        rng.remove(j)

    full_order.extend(rng)
    mod_order = []

    for i in range(op_cnt):
        cnt = 0
        for j in range(i):
            if full_order[j] < full_order[i]:
                cnt += 1
        mod_order.append(full_order[i] - cnt)

    result = calc_ints[0]
    for i in mod_order:
        if calc_ops[i] == '+':
            result = calc_ints[i] + calc_ints[i + 1]
        elif calc_ops[i] == '*':
            result = calc_ints[i] * calc_ints[i + 1]
        elif calc_ops[i] == '-':
            result = calc_ints[i] - calc_ints[i + 1]
        else:
            raise Exception
        calc_ints[i] = result
        calc_ints.pop(i + 1)
        calc_ops.pop(i)
    return result


N = int(sys.stdin.readline())
s = list(str(sys.stdin.readline()))

op_cnt = N // 2

ops = []
ints = []
for i in range(N):
    if i % 2 == 1:
        ops.append(s[i])
    else:
        ints.append(int(s[i]))

print(dfs([], -2, op_cnt))



# def dfs(ops: list, ints: list, op_l: int) -> int:
#     if op_l == 0:
#         return ints[0]
#     else:
#         results = []
#         for i in range(op_l):
#             if ops[i] == '+':
#                 result = ints[i] + ints[i + 1]
#             elif ops[i] == '*':
#                 result = ints[i] * ints[i + 1]
#             elif ops[i] == '-':
#                 result = ints[i] - ints[i + 1]
#             else:
#                 raise Exception
#
#             ops_i = ops.copy()
#             ints_i = ints.copy()
#             ops_i.pop(i)
#             ints_i[i] = result
#             ints_i.pop(i + 1)
#
#             results.append(dfs(ops_i, ints_i, op_l - 1))
#         return max(results)
#
# if __name__ == '__main__':
#
#     N = int(sys.stdin.readline())
#     s = list(str(sys.stdin.readline()))
#
#     op_cnt = N // 2
#
#     ops = []
#     ints = []
#     for i in range(N):
#         if i % 2 == 1:
#             ops.append(s[i])
#         else:
#             ints.append(int(s[i]))
#
#     print(dfs(ops, ints, op_cnt))
