class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1)+1, len(s2)+1
        if len(s3) != l1+l2-2:
            return False
        dp = [[False]*l2 for _ in range(l1)]
        dp[0][0] = True
        for i in range(1, l1): dp[i][0] = dp[i-1][0] and (s1[i-1] == s3[i-1])
        for j in range(1, l2): dp[0][j] = dp[0][j-1] and (s2[j-1] == s3[j-1])
        for i in range(1,l1):
            for j in range(1,l2):
                dp[i][j] = ((s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1]))
        return dp[-1][-1]
    
# at dp[i][j] we use s1[:i] -> i characters; s2[:j] -> j characters and s3[:i+j] -> i+j characters