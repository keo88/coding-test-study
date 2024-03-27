# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        target = len(arr) - n

        if target > 0:
            arr[target - 1].next = arr[target].next
        else:
            head = arr[0].next
        return head
