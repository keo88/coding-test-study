# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        arr.sort(key=lambda x: x.val)

        prev = None
        for item in arr:
            if prev:
                prev.next = item
            prev = item
        arr[-1].next = None
        return arr[0]
