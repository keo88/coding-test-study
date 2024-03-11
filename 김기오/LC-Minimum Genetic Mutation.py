from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        dq = deque([(startGene, 0)])
        visited = {}
        while dq:
            gene, depth = dq.popleft()
            if gene in visited:
                continue
            visited[gene] = depth
            if gene == endGene:
                return depth

            for item in bank:
                totDiff = 0
                for i in range(len(item)):
                    totDiff += gene[i] != item[i]
                if totDiff == 1:
                    dq.append((item, depth + 1))
        return -1
                
