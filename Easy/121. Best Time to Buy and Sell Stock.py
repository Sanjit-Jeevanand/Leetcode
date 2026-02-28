class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min, max_profit = prices[0],0
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i] - min > max_profit: 
                max_profit = prices[i] - min
        return max_profit
    
# Running Mimimum / Prefix Optimisation Pattern
# Keep a minimum until a new ones arrives; if any further profit beats it; replace the profit