import sys

sys.setrecursionlimit(10**6)
N = int(input())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))
rootNum = [0] * (N + 1)

for i in range(len(inorder)):
    rootNum[inorder[i]] = i


def divide_conquer(in_start: int, post_start: int, length: int):
    if length <= 0:
        return
    root = postorder[post_start + length - 1]
    in_root_index = rootNum[root]

    left_length = in_root_index - in_start
    right_length = length - left_length - 1
    print(root, end=' ')
    divide_conquer(in_start, post_start, left_length)
    divide_conquer(in_root_index + 1, post_start + left_length, right_length)


divide_conquer(0, 0, len(inorder))
