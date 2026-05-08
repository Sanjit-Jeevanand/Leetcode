class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S%2 != 0: return False
        S //= 2
        n = len(nums)
        dp = [[False]*(S+1) for _ in range(n+1)]
        for i in range(n+1): dp[i][0] = True
        for i in range(1,n+1):
            for x in range(1,S+1):
                if x-nums[i-1] >= 0:
                    dp[i][x] = dp[i-1][x-nums[i-1]] or dp[i-1][x]
                else:
                    dp[i][x] = dp[i-1][x]
        return dp[n][S]
    
# Interval DP