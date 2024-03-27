# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        def flattenWithLast(top: TreeNode) -> TreeNode:
            last = top
            topRight = top.right
            if top.left:
                last = flattenWithLast(top.left)
                top.right = top.left
                top.left = None
            if topRight:
                rt = flattenWithLast(topRight)
                last.right = topRight
                last = rt
            return last

        flattenWithLast(root)
        """
        Do not return anything, modify root in-place instead.
        """
        
