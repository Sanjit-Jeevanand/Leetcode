class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        dist = [float('inf')] * n
        dist[src] = 0
        q = deque([(src, 0)])
        stops = 0
        while q and stops <= k:
            size = len(q)
            for _ in range(size):
                u, cost = q.popleft()
                for v,w in graph[u]:
                    if cost+w < dist[v]:
                        dist[v] = cost+w
                        q.append((v,dist[v]))
            stops += 1
        return -1 if dist[dst] == float('inf') else dist[dst]