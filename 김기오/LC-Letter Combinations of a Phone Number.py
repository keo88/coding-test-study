class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        arrs = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = [''] * len(digits)
        ans = []
        
        def dfs(i: int):
            if i == len(digits):
                ans.append(''.join(res))
                return
            
            arr = arrs[digits[i]]
            for ach in arr:
                res[i] = ach
                dfs(i + 1)
        
        dfs(0)
        return ans
            

