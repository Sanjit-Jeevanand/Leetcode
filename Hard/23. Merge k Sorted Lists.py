# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
        dummy = ListNode()
        curr = dummy
        while h:
            _, x = heapq.heappop(h)
            curr.next = lists[x]
            lists[x] = lists[x].next
            if lists[x]:
                heapq.heappush(h, (lists[x].val, x))
            curr = curr.next
        return dummy.next
        
# lists[i].val, i since heap cannot compare listnodes