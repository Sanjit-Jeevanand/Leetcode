class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can(k) -> int:
            return sum(ceil(x/k) for x in piles) <= h
        l = 1
        r = max(piles)
        while l < r:
            m = (l+r)//2
            if can(m):
                r = m
            else:
                l = m + 1
        return l
    
# Define the function:
# Here: hours = Σ ceil(pile / speed)
# Rest is normal binary search