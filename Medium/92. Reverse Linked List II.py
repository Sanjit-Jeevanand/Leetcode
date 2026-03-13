# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        tail = curr
        prev_rev = None
        for _ in range(right - left + 1):
            nextn = curr.next
            curr.next = prev_rev
            prev_rev = curr
            curr = nextn
        prev.next = prev_rev
        tail.next = curr
        return dummy.next
    
# Reversed Linked List with Specific L and R
# Use Dummy Node to avoid edge cases