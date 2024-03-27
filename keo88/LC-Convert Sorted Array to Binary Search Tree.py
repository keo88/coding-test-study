# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def construct(left: int, right: int):
            if left == right:
                return TreeNode(nums[left])
            elif left + 1 == right:
                return TreeNode(nums[right], TreeNode(nums[left]))
            mid  = (left + right) // 2
            # print(left, mid, right)
            leftTree = construct(left, mid - 1)
            rightTree = construct(mid + 1, right)
            return TreeNode(nums[mid], leftTree, rightTree)
        
        if not nums:
            return None
        return construct(0, len(nums) - 1)

