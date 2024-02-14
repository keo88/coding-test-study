class Solution:
    def hIndex(self, citations: List[int]) -> int:
        scores = sorted(citations)
        l = len(scores)
        ans = 0

        for i, s in enumerate(scores):
            cnt = l - i
            ans = max(ans, min(cnt, s))

        return ans
        
