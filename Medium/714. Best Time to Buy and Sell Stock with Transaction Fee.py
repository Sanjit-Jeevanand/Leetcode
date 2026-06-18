class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        n = len(prices)
        def solve(i,h):
            if i == n: return 0
            if (i,h) in memo: return memo[(i,h)]
            if h:
                memo[(i,h)] = max(solve(i+1,h),solve(i+1,0)+prices[i]-fee)
            else:
                memo[(i,h)] = max(solve(i+1,h), solve(i+1,1) - prices[i])
            return memo[(i,h)]
        return solve(0,0)