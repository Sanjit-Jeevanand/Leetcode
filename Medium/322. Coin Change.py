class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1, amount+1):
            mini = float('inf')
            for x in coins:
                if x <= i:
                    mini = min(dp[i-x]+1,mini)
            dp[i] = mini
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
    
# Linear DP