class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        last = points[0]
        ans = []
        for i in range(1, len(points)):
            p = points[i]
            if p[0] <= last[1]:
                last[0] = p[0]
                last[1] = min(p[1], last[1])
            else:
                ans.append(last)
                last = p
        ans.append(last)
        return len(ans)
