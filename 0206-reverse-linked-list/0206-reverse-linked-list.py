# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back = None
        curr = front = head
        while curr:
            front = curr.next
            curr.next = back
            back = curr
            curr = front
        return back