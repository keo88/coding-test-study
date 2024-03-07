# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([(root, 0)])
        ans = []

        while q:
            node, depth = q.popleft()
            if depth >= len(ans):
                ans.append([node.val])
            else:
                ans[depth].append(node.val)
            
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        
        for i in range(1, len(ans), 2):
            ans[i].reverse()
        return ans
