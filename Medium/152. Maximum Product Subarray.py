class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def solve(i):
            if i == 0: 
                memo[i] = (nums[0],nums[0])
                return memo[i]
            if i in memo: return memo[i]
            x,y = solve(i-1)
            x *= nums[i]
            y *= nums[i]
            memo[i] = (max(x,y,nums[i]),min(x,y,nums[i]))
            return memo[i]
        solve(n-1)
        return max(memo.values())[0]
        