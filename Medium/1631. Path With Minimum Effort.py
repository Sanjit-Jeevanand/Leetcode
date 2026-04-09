class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dist = [[float('inf')]*n for _ in range(m)]
        dist[0][0] = 0
        h = [(0,0,0)]
        while h:
            effort, r, c = heappop(h)
            if (r,c) == (m-1,n-1):
                return effort
            if effort > dist[r][c]:
                continue
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    diff = abs(grid[nr][nc] - grid[r][c])
                    n_effort = max(effort, diff)
                    if n_effort < dist[nr][nc]:
                        dist[nr][nc] = n_effort
                        heappush(h, (n_effort, nr, nc))
        return dist[m-1][n-1]
    
# Dijkstra's Algorithm
# Graph-Optimisation Problem