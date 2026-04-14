class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 1
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    if j-i+1 > max_len:
                        start = i
                        max_len = j-i+1
                    dp[i][j] = True
        return s[start:start+max_len]
    
# 2D DP