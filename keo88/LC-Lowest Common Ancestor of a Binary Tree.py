# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        skip = False
        
        def dfs(node: 'TreeNode'):
            nonlocal skip, ans
            if skip:
                return True, True
            
            lres, rres = False, False

            if node.left:
                lres, rres = dfs(node.left)
            if node.right:
                l, r = dfs(node.right)
                lres, rres = l or lres, r or rres
            if skip:
                return True, True
            
            lres, rres = lres or p.val == node.val, rres or q.val == node.val
            if lres and rres:
                skip = True
                ans = node
            return lres, rres
        
        if root:
            dfs(root)
        return ans
