# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        
        newHead = Node(head.val)
        prevNewCur = newHead
        cur = head.next
        mapping = {
            head: newHead
        }
        while cur:
            newCur = Node(cur.val)
            prevNewCur.next = newCur
            mapping[cur] = newCur
            
            prevNewCur = newCur
            cur = cur.next
        
        cur = head
        newCur = newHead
        while cur:
            if cur.random:
                newCur.random = mapping[cur.random]

            newCur = newCur.next
            cur = cur.next
        return newHead
        
                    
