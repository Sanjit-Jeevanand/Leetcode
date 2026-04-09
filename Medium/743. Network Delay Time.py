class Solution:
    def networkDelayTime(self, times, n, k):
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]
        while heap:
            dist_u, u = heappop(heap)
            if dist_u > dist[u]:
                continue
            for v, w in graph[u]:
                if dist_u + w < dist[v]:
                    dist[v] = dist_u + w
                    heappush(heap, (dist[v], v))
        max_dist = max(dist[1:])
        return -1 if max_dist == float('inf') else max_dist
    
# Djikstra's Algorithm
# Heap to get the minimum distance