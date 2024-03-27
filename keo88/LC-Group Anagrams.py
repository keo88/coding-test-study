class Solution:
    def extractId(self, s: str) -> str:
        return ''.join(sorted(list(s)))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for s in strs:
            sId = self.extractId(s)
            if sId in d:
                d[sId].append(s)
            else:
                d[sId] = [s]
        ans = []
        for k in d:
            ans.append(d[k])
        return ans
