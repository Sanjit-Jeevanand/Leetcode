class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        a,b = nums[0], max(nums[0],nums[1])
        for i in range(2,n):
            a,b = b, max(a+nums[i],b)
        return b
    
# Linear DP
# For base case; find answers to 2 smallest possible cases
# dp[i] = max(dp[i-1], dp[i-2]+nums[i])