class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        n = len(s)
        d = {}
        for i in range(n):
            d[s[i]] = d.get(s[i],0) + 1
            d[t[i]] = d.get(t[i],0) - 1
        return all(x == 0 for x in d.values())