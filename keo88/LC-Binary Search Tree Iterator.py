# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.index = -1
        
        def inorder(node: TreeNode):
            if node.left:
                inorder(node.left)
            self.arr.append(node.val)
            if node.right:
                inorder(node.right)
        
        if root:
            inorder(root)

    def next(self) -> int:
        self.index += 1
        return self.arr[self.index]

    def hasNext(self) -> bool:
        if self.index < len(self.arr) - 1:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
