class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        o = c = 0
        ans = []
        
        def dfs(o: int, c: int, s: str):
            if o == 0 and c == 0:
                ans.append(s)

            if o > 0:
                dfs(o - 1, c + 1, s + '(')
            if c > 0:
                dfs(o, c - 1, s + ')')
        dfs(n, 0, '')
        return ans

