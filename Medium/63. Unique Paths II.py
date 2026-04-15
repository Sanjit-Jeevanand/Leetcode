class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        if grid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]
    
# Same as Unique Paths but dp[obstacle] == 0