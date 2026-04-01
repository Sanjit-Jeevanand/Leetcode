class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid), len(grid[0])
        visited = set()
        def dfs(i,j, pi, pj):
            if (i, j) in visited:
                return True
            visited.add((i,j))
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == grid[i][j]:
                    if (ni, nj) == (pi, pj):
                        continue
                    if dfs(ni,nj, i, j):
                        return True
            return False
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited:
                    if dfs(i, j, -1, -1):
                        return True
        return False
    
# DFS Cycle detection on Grid via Parent Tracking