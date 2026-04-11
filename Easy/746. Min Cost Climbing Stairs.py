class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        a = cost[0]
        b = cost[1]
        for i in range(2,n):
            a,b = b, cost[i] + min(b, a)
        return min(a,b)
    
# 1D DP
# Base cases depend on state definition