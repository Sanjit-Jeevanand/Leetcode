class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev = defaultdict(list)
        outdegree = [0] * n
        for u in range(n):
            outdegree[u] = len(graph[u])
            for v in graph[u]:
                rev[v].append(u)  
        q = deque()
        for i in range(n):
            if outdegree[i] == 0:
                q.append(i)
        safe = []
        while q:
            u = q.popleft()
            safe.append(u)
            for v in rev[u]:
                outdegree[v] -= 1
                if outdegree[v] == 0:
                    q.append(v)
        return sorted(safe)
    
# Kahn’s Topological Sort — applied on reversed graph with outdegree