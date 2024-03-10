class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = {}
        for preq in prerequisites:
            to, frm = preq
            if not frm in nodes:
                nodes[frm] = []    
            if not to in nodes:
                nodes[to] = []
            nodes[frm].append(to)
        
        checked = {}

        def dfs(cur: int, visited: Set[int]):
            if cur in checked:
                return checked[cur]
            if cur in visited:
                checked[cur] = True
                return True
            
            visited.add(cur)
            ans = False
            for nbr in nodes[cur]:
                ans = ans or dfs(nbr, visited)
            visited.remove(cur)
            checked[cur] = ans
            return ans
        
        res = False
        visited = set()
        for node in nodes:
            res = res or dfs(node, visited)
            if res:
                break
        return not res
