# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr = []
        cur = head
        while cur:
            arr.append(cur)
            cur = cur.next
        
        if left > 1:
            arr[left - 2].next = arr[right - 1]
        if right == len(arr):
            arr[left - 1].next = None
        else:
            arr[left - 1].next = arr[right]
        for i in range(left, right):
            arr[i].next = arr[i - 1]
        return head if left != 1 else arr[right - 1]
        
