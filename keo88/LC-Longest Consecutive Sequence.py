class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sNums = sorted(nums)
        acc = 1
        ans = 1
        for i in range(1, len(sNums)):
            if sNums[i - 1] + 1 == sNums[i]:
                acc += 1
                ans = max(ans, acc)
            elif sNums[i - 1] == sNums[i]:
                continue
            else:
                acc = 1
        return ans     
