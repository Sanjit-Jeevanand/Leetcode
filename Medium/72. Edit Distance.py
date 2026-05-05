class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1)+1,len(s2)+1
        dp = [[0]*l2 for _ in range(l1)]
        for i in range(l1):
            dp[i][0] = i
        for j in range(l2):
            dp[0][j] = j
        for i in range(1,l1):
            for j in range(1,l2):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        return dp[-1][-1]
    
# Alignment DP