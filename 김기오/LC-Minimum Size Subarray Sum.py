class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        length = len(nums)
        acc = nums[0]
        ans = 100001
        while True:
            if acc < target:
                r += 1
                if r >= length:
                    break
                acc += nums[r]
            elif acc >= target:
                ans = min(ans, r - l + 1)
                acc -= nums[l]
                l += 1
        return 0 if ans == 100001 else ans
                
