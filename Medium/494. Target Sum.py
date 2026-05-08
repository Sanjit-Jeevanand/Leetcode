class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        x = target + sum(nums)
        if x%2 == 1 or x < 0:
            return 0 
        p = x//2
        dp = [[0]*(p+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1,n+1):
            for x in range(p+1):
                if x - nums[i-1] >= 0:
                    dp[i][x] += dp[i-1][x-nums[i-1]]
                dp[i][x] += dp[i-1][x]
        return dp[n][p]