# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        low = lowHead = highHead = high = None
        cur = head
        while cur:
            if cur.val < x:
                if low:
                    low.next = cur
                    low = low.next
                else:
                    low = lowHead = cur
            else:
                if high:
                    high.next = cur
                    high = high.next
                else:
                    high = highHead = cur
            cur = cur.next
        if high:
            high.next = None
        if low:
            low.next = highHead
        return lowHead if lowHead else highHead

        
