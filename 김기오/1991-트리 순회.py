import sys


class Node:
    def __init__(self, id: str):
        self.id = id
        self.left = None
        self.right = None


def preorder(node: Node):
    if node:
        print(node.id, end='')
        preorder(node.left)
        preorder(node.right)


def inorder(node: Node):
    if node:
        inorder(node.left)
        print(node.id, end='')
        inorder(node.right)


def postorder(node: Node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.id, end='')


N = int(input())
trees = {}

for i in range(N):
    parent, child1, child2 = sys.stdin.readline().split()
    if parent in trees:
        parent_node = trees[parent]
    else:
        parent_node = Node(parent)
        trees[parent] = parent_node

    if child1 != '.':
        if child1 in trees:
            child_node1 = trees[child1]
        else:
            child_node1 = Node(child1)
            trees[child1] = child_node1
        parent_node.left = child_node1
    if child2 != '.':
        if child2 in trees:
            child_node2 = trees[child2]
        else:
            child_node2 = Node(child2)
            trees[child2] = child_node2
        parent_node.right = child_node2


preorder(trees['A'])
print()
inorder(trees['A'])
print()
postorder(trees['A'])