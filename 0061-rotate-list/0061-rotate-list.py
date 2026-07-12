# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        ptr = head
        n = 1
        while ptr.next:
            n += 1
            ptr = ptr.next
        k = k % n
        ptr.next = head
        tail_pos = n -k 
        curr = head
        for _ in range(tail_pos):
            prev = curr
            curr = curr.next
        prev.next = None
        return curr