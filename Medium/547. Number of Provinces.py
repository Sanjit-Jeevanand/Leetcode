class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        n = len(isConnected)
        parent = [0]*n
        for i in range(len(isConnected)):
            parent[i] = i
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i,j)
        return len(set(find(i) for i in range(n)))
        

# Unioon - Find Problem
# Graph - Connectivity Pattern