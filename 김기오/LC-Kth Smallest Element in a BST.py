# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        left = {}

        def postorder(node: TreeNode) -> int:
            s = 0
            if node.left:
                s += postorder(node.left)
            left[node] = s
            if node.right:
                s += postorder(node.right)
            return 1 + s
        
        postorder(root)
        # print(list((item.val, left[item]) for item in left))

        curNode = root
        while left[curNode] + 1 != k:
            if k <= left[curNode]:
                curNode = curNode.left
            elif k > left[curNode]:
                k -= left[curNode] + 1
                curNode = curNode.right
        return curNode.val
            



