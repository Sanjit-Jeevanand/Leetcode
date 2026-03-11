class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def can(t) -> bool:
            return sum(t // x for x in time) >= totalTrips
        l = 1
        r = totalTrips*(min(time))
        while l < r:
            m = (l+r)//2
            if can(m):
                r = m
            else:
                l = m + 1
        return l