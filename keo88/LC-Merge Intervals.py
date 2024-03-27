class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        last = intervals[0]
        ans = [last]
        for interval in intervals:
            if interval[0] <= last[1]:
                last[1] = max(last[1], interval[1])
            else:
                last = interval
                ans.append(last)
        return ans
