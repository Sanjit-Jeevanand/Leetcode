class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        points = [0]+sorted(cuts)+[n]
        x = len(points)
        dp = [[0]*x for _ in range(x)]
        for length in range(2, x):
            for i in range(x - length):
                j = i + length
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i+1,j)) + points[j] - points[i]
        return dp[0][x-1]
    
# Interval DP