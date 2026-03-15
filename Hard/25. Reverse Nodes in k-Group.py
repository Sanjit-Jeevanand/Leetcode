# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy
        while True:
            curr = prev_group
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next
            tail = prev_group.next
            curr = tail
            prev = None
            for _ in range(k):
                nextn = curr.next
                curr.next = prev
                prev = curr
                curr = nextn
            prev_group.next = prev
            tail.next = curr
            prev_group = tail

# Check if k future nodes exist
# If they do reverse the next k nodes
# Attach head of reverse
# Attach tail of reverse to new node
# Set prev_group to tail