# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        front = head
        back = head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        prev = dummy
        for _ in range(n):
            front = front.next
        
        while front:
            prev = back
            back = back.next
            front = front.next

        prev.next = prev.next.next
        return head.next