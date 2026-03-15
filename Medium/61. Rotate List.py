# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head
        k = k % n
        steps = n - k
        curr = head
        for _ in range(steps - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        return new_head
    
# Find n -> Make it Circular -> Break after k%n - 1 steps; assign next pointer as the new head