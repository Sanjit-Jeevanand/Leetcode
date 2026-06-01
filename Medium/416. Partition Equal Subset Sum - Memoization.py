class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S%2 == 1: return False
        S //= 2
        memo = {}
        def cp(S,i):
            if S == 0:
                return True
            if i < 0 or S < 0:
                return False
            if (S,i) in memo:
                return memo[(S,i)]
            else:
                memo[(S,i)] = cp(S-nums[i],i-1) or cp(S,i-1)
            return memo[(S,i)]
        return cp(S,len(nums)-1)
    
# 0/1 Knapsack - Memoization Solution