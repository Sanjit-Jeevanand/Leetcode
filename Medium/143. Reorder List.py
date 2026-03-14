# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        sp = head
        fp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        prev = None
        curr = sp.next
        sp.next = None
        while curr:
            nextn = curr.next
            curr.next = prev
            prev = curr
            curr = nextn
        first = head
        second = prev
        while second:
            t1 = first.next
            t2 = second.next
            first.next = second
            second.next = t1
            first = t1
            second = t2