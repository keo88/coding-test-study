class Solution:
    def myCombinations(self, arr: List[int], r: int) -> List[List[int]]:

        ans = []
        cur = []
        def backtrack(first: int):
            if len(cur) == r:
                ans.append(cur[:])
                return
            for i in range(first, len(arr)):
                cur.append(arr[i])
                backtrack(i + 1)
                cur.pop()
        backtrack(0)
                
        return ans

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.myCombinations(list(range(1, n + 1)), k)
        
