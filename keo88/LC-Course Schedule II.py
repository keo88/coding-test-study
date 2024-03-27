

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        reqs = [0] * numCourses
        nbrs = [[] for _ in range(numCourses)]

        for preq in prerequisites:
            to, frm = preq
            reqs[to] += 1
            nbrs[frm].append(to)
        
        starts = []
        for i, req in enumerate(reqs):
            if req == 0:
                starts.append(i)
        
        for s in starts:
            reqs[s] += 1
        
        ans = []
        dq = deque(starts)
        while dq:
            node = dq.popleft()
            reqs[node] -= 1
            if reqs[node] == 0:
                ans.append(node)
                for nbr in nbrs[node]:
                    dq.append(nbr)
        
        if sum(reqs) != 0:
            return []
        else:
            return ans

            

