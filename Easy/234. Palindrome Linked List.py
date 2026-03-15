# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        sp = head
        fp = head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        curr = sp.next
        sp.next = None
        prev = None
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        first = head
        second = prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True
    
# Use fp = head.next to land at node before the middle one