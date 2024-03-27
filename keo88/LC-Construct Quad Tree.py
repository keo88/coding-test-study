"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def constructTree(x: int, y: int, l: int) -> 'Node':
            if l == 1:
                return Node(grid[x][y], True)
            
            nl = l // 2
            subtrees = []
            subtrees.append(constructTree(x, y, nl))
            subtrees.append(constructTree(x, y + nl, nl))
            subtrees.append(constructTree(x + nl, y, nl))
            subtrees.append(constructTree(x + nl, y + nl, nl))
            if all(t.isLeaf for t in subtrees):
                fVal = subtrees[0].val
                isSame = True
                for i in range(1, 4):
                    if fVal != subtrees[i].val:
                        isSame = False
                        break
                
                if isSame:
                    return Node(fVal, True)
            return Node(0, False, subtrees[0], subtrees[1], subtrees[2], subtrees[3])
        
        return constructTree(0, 0, len(grid))




