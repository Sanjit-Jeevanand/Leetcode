class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can(x) -> bool:
            psum = 0
            k = 1
            for i in weights:
                psum += i
                if psum > x:
                    k += 1
                    psum = i
            return k <= days
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l+r)//2
            if can(m):
                r = m
            else:
                l = m + 1
        return l
    
# Binary Search on answer Space
# Remember boundary condition and r = m comes first
# psum -> if more than capacity; it is transferred the next day
# l should be max(weight) else the biggest one would never be transferred