class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo = {}
        n = len(prices)
        def solve(i,h,l):
            if i == n: return 0
            if (i,h,l) in memo: return memo[(i,h,l)]
            if l == k:
                memo[(i,h,l)] = solve(i+1,h,l)
            else:
                if h:
                    memo[(i,h,l)] = max(solve(i+1,h,l), solve(i+1,0,l+1) + prices[i])
                else:
                    memo[(i,h,l)] = max(solve(i+1,h,l), solve(i+1,1,l) - prices[i])
            return memo[(i,h,l)]
        return solve(0,0,0)