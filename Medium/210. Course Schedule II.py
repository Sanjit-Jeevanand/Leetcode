class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0]*n
        q = deque()
        for a,b in prereq:
            graph[b].append(a)
            indegree[a] += 1
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        processed = []
        while q:
            u = q.popleft()
            processed.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return processed if len(processed) == n else []

# Kahn's Algorithm