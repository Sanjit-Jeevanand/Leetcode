class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*(n) for _ in range(n)]
        for length in range(1,n):
            for i in range(n - length):
                j = i+length
                if j - i > 1:
                    dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j] for k in range(i+1,j))
        return dp[0][n-1]
    
# Interval DP