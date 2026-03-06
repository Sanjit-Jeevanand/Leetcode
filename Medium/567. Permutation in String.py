class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in s1:
            d1[i] += 1
        k = len(s1)
        l = 0
        for i in range(len(s2)):
            d2[s2[i]] += 1
            while i - l >= k:
                d2[s2[l]] -= 1
                if(d2[s2[l]] == 0):
                    d2.pop(s2[l])
                l += 1
            if d1 == d2:
                return True
        return False

# Sliding Window + Hashmap