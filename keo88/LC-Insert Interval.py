class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        ans = []
        isStart = True
        startRange = endRange = -1
        startInd = -1
        for i, interval in enumerate(intervals):
            if isStart:
                if newInterval[0] <= interval[1]:
                    startRange = min(interval[0], newInterval[0])
                    isStart = False
                else:
                    ans.append(interval)
                    continue
            if not isStart:
                if newInterval[1] < interval[0]:
                    if i > 0:
                        endRange = max(newInterval[1], intervals[i - 1][1])
                    else:
                        endRange = newInterval[1]
                    break
        if endRange == -1:
            endRange = max(newInterval[1], intervals[-1][1])
            i += 1
        if isStart:
            startRange = newInterval[0]
        ans.append([startRange, endRange])
        ans.extend(intervals[i:])
        
        return ans
