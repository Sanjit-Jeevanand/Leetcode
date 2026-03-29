class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i in points:
            heapq.heappush(h, (-(i[0]**2 + i[1]**2), i))
            if len(h) > k:
                heapq.heappop(h)
        return [x for _,x in h]
        

# Max Heap
# Return Function