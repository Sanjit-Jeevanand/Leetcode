class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones) 
        s = total // 2
        dp = [False]*(s+1)
        dp[0] = True
        for stone in stones:
            for x in range(s, stone - 1, -1):
                dp[x] = dp[x] or dp[x-stone]
        best = 0
        for x in range(s, -1, -1):
            if dp[x]:
                best = x
                break
        return total - 2*best
    
# Knapsack