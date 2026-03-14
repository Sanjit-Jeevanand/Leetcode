# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        dummy.next = curr
        for _ in range(n):
            curr = curr.next
        nnode = dummy
        while curr:
            curr = curr.next
            nnode = nnode.next
        nnode.next = nnode.next.next
        return dummy.next