class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        heap = [(0,src,0)]
        ans = float('inf')
        while heap:
            cost, node, stops = heappop(heap)
            if node == dst:
                ans = min(ans, cost)
                continue
            if stops > k:
                continue
            for v,w in graph[node]:
                heappush(heap,(cost+w, v, stops+1))
        return -1 if ans == float('inf') else ans

# Dijkstra