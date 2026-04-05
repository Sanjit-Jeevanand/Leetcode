class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootY != rootX:
                parent[rootY] = rootX
        n = len(edges)
        parent = [0]*(n+1)
        for i in range(n+1):
            parent[i] = i
        for u,v in edges:
            if find(u) == find(v):
                return [u,v]
            else:
                union(u,v)
        return ans
    
# Union-Find
# Graph Connectivity