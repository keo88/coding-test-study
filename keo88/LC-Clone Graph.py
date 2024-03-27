"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        newNodes = {}
        dq = deque([node])
        while dq:
            nd = dq.popleft()
            if nd in newNodes:
                continue
            newNodes[nd] = Node(nd.val)
            for nbr in nd.neighbors:
                dq.append(nbr)
        
        for nd in newNodes:
            newNodes[nd].neighbors = list(newNodes[ndk] for ndk in nd.neighbors)
        
        return newNodes[node]
