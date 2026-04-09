class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dist = [[float('inf')]*n for _ in range(n)]
        h = [(grid[0][0],0,0)]
        dist[0][0] = grid[0][0]
        while h:
            effort, i,j = heappop(h)
            if effort > dist[i][j]:
                continue
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj = i+di,j+dj
                if 0 <= ni < n and 0 <= nj < n:
                    n_effort = max(effort, grid[ni][nj])
                    if n_effort < dist[ni][nj]:
                        dist[ni][nj] = n_effort
                        heappush(h,(n_effort, ni,nj))
        return dist[n-1][n-1]

# Dijkstra - Max Variant
# Dijkstra allows revisiting of old nodes; but only updates them if effort is lower