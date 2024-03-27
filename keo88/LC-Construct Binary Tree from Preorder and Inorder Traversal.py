# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = preorder[0]
        rootInd = inorder.index(root)
        leftTree = self.buildTree(preorder[1:1+rootInd], inorder[:rootInd])
        rightTree = self.buildTree(preorder[1+rootInd:], inorder[rootInd+1:])
        return TreeNode(root, leftTree, rightTree)
