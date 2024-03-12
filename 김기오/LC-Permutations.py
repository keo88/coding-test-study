class Solution:
    def myCombinate(self, nums: List[int], r: int):
        res = []
        ans = []

        def backtrack(first: int):
            if len(res) == r:
                ans.append(res[:])

            for i in range(first, len(nums)):
                res.append(nums[i])
                backtrack(i + 1)
                res.pop()
        backtrack(0)
        return ans

    def myPermute(self, nums: List[int], r: int):
        used = [False] * len(nums)
        res = []
        ans = []
        def backtrack():
            if len(res) == r:
                ans.append(res[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                res.append(nums[i])
                backtrack()
                res.pop()
                used[i] = False
        backtrack()

        return ans


    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.myPermute(nums, len(nums))
