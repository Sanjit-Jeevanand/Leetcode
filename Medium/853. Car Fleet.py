class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        t = []
        d = {}  
        n = len(speed)
        ans = 0
        for i in range(n):
            d[position[i]] = speed[i]
        t = sorted(position)
        for i in range(n):
            t[i] = (target - t[i])/d[t[i]]
        for i in range(n-2,-1,-1):
            t[i] = max(t[i],t[i+1])
        s = set(t)
        return len(s)

# Time = distance/speed