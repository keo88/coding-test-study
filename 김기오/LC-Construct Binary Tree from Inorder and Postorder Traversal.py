# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderMap = {inorder[i]: i for i in range(len(inorder))}

        def build(postorder: List[int], iStart: int, iEnd: int):
            if not postorder or iStart > iEnd:
                return None
            root = postorder.pop()
            rootInd = inorderMap[root]
            rightTree = build(postorder, rootInd + 1, iEnd)
            leftTree = build(postorder, iStart, rootInd - 1)
            return TreeNode(root, leftTree, rightTree)
        
        return build(postorder, 0, len(inorder) - 1)

