class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        디코안녕 = [nums[0]]
        for i in range(1, len(nums)):
            디코안녕.append(max(nums[i], nums[i] + 디코안녕[i - 1]))
        return max(디코안녕)