# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        cut = len(arr) - (k % len(arr))
        if cut == len(arr):
            return head
        arr[cut - 1].next = None
        arr[len(arr) -  1].next = head
        newHead = arr[cut]

        return newHead
        

