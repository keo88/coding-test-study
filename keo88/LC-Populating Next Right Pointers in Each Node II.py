"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        d = deque([(root, 1)])
        prev, prevNode = 0, None
        
        while d:
            node, depth = d.popleft()
            if depth == prev and prevNode:
                prevNode.next = node
            prev, prevNode = depth, node

            if node.left:
                d.append((node.left, depth + 1))
            if node.right:
                d.append((node.right, depth + 1))
        return root

