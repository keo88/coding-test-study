class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, len(nums)):
            dp.append(nums[i] + max(dp[-2], dp[-3]))

        return max(dp[-1], dp[-2])
