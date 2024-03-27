# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def sumAcc(acc: int, root: TreeNode) -> int:
            nextAcc = acc * 10 + root.val
            s = 0
            if root.left:
                s += sumAcc(nextAcc, root.left)
            if root.right:
                s += sumAcc(nextAcc, root.right)
            if not root.left and not root.right:
                s = nextAcc
            return s
        
        if not root:
            return 0
        
        return sumAcc(0, root)
