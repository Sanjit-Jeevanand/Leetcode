class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        d1 = {}
        n = len(s)
        if n != len(t):
            return False
        for i in range(n):
            if s[i] not in d:
                d[s[i]] = t[i]
            elif d[s[i]] != t[i]:
                return False
            if t[i] not in d1:
                d1[t[i]] = s[i]
            elif d1[t[i]] != s[i]:
                return False
        return True
    
# Saving and checking previous mappings on both strings to ensure one-to-one