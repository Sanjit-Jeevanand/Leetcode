class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        W = (sum(nums)+target)
        if W < 0 or W%2: return 0
        W //= 2
        memo = {}
        def ts(i,W):
            if i < 0:
                return 1 if W == 0 else 0
            if (i,W) in memo: return memo[(i,W)]
            if W - nums[i] < 0: 
                memo[(i,W)] = ts(i-1,W)
                return memo[(i,W)]
            else: 
                memo[(i,W)] = ts(i-1,W-nums[i]) + ts(i-1,W)
                return memo[(i,W)]
        return ts(len(nums)-1, W)
    
# Knapsack - Memoization