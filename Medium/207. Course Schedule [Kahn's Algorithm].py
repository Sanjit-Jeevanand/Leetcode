class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*n
        q = deque()
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]] += 1
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        if len(q) == 0:
            return False
        processed = 0
        while q:
            u = q.popleft()
            processed += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return n == processed