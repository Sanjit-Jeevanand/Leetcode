class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        ans = []
        for i in nums:
            d[i] += 1
        h = []
        for v, f in d.items():
            heapq.heappush(h, (f, v))
            if len(h) > k:
                heapq.heappop(h)
        for i in h:
            ans.append(i[1])
        return ans
    
# Heap with custom priority