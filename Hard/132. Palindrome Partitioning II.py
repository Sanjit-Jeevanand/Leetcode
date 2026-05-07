class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dph = [[False]*(n) for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dph[i+1][j-1]):
                    dph[i][j] = True
        for i in range(1,n+1):
            j = 0
            while j < i:
                if dph[j][i-1]:
                    dp[i] = min(dp[i], dp[j]+1)
                j += 1
        return dp[-1] - 1
    
# 1D DP with 2D helper DP