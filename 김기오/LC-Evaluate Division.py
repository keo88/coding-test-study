from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        nodes = {}

        for i in range(len(equations)):
            eq, val = equations[i], values[i]
            ch1, ch2 = eq
            if not ch1 in nodes:
                nodes[ch1] = {}
            if not ch2 in nodes:
                nodes[ch2] = {}
            nodes[ch1][ch2] = val
            nodes[ch2][ch1] = 1 / val
        
        ans = []
        for query in queries:
            ch1, ch2 = query
            if not ch1 in nodes or not ch2 in nodes:
                ans.append(-1.0)
                continue
            
            dq = deque([(ch1, 1.0)])
            visited = set()
            found = False
            while dq:
                c, r = dq.popleft()
                if c in visited:
                    continue
                visited.add(c)
                if c == ch2:
                    ans.append(r)
                    found = True
                    break

                for nbr in nodes[c]:
                    dq.append((nbr, r * nodes[c][nbr]))

            if not found:
                ans.append(-1.0)
        return ans
