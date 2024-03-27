class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans, res = [], []

        def backtrack(first: int, acc: int):
            if acc == target:
                ans.append(res[:])
                return
            elif acc > target:
                return

            for i in range(first, len(candidates)):
                res.append(candidates[i])
                backtrack(i, acc + candidates[i])
                res.pop()
        backtrack(0, 0)
        return ans
