class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lastInt = (-2) ** 31 - 1
        def inorder(node: Optional[TreeNode]):
            nonlocal lastInt
            if not node:
                return True
            res = inorder(node.left)
            if not res:
                return False
            if lastInt >= node.val:
                return False
            else:
                lastInt = node.val
            res = inorder(node.right)
            return res
        
        return inorder(root)
