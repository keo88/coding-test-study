# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        ans = ansHead = None
        while cur:
            isDup = False
            curVal = cur.val
            while cur.next and cur.next.val == curVal:
                isDup = True
                cur = cur.next
            if not isDup:
                if ans:
                    ans.next = cur
                    ans = ans.next
                else:
                    ansHead = cur
                    ans = cur
            cur = cur.next
        
        if ans:
            ans.next = None
        return ansHead
