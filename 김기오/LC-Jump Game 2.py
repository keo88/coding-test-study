class Solution:
    def jump(self, nums: List[int]) -> int:
        intMax = 10 ** 4 + 1
        dp = [intMax] * len(nums)
        dp[-1] = 0
        
        for i in range(len(nums) - 2, -1, -1):
            val = nums[i]
            minList = list(dp[j] for j in range(i + 1,min(len(nums), i + val + 1)))
            # print(minList)
            dp[i] = min(minList) + 1 if minList else intMax
        
        return dp[0]
