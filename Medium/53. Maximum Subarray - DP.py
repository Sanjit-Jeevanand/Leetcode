class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def solve(i):
            if i == 0:
                memo[0] = nums[0]
                return nums[0]
            if i in memo: return memo[i]
            memo[i] = max(solve(i-1)+nums[i],nums[i])
            return memo[i]
        solve(n-1)
        return max(memo.values())