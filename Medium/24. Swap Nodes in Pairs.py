# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            f = prev.next
            s = prev.next.next
            f.next = s.next
            s.next = f
            prev.next = s
            prev = f
        return dummy.next
    
# Using prev as dummy node