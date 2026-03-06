class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in p:
            d1[i] += 1
        l = 0
        k = len(p)
        ans = []
        for i in range(len(s)):
            d2[s[i]] += 1
            while i - l >= k:
                d2[s[l]] -= 1
                if d2[s[l]] == 0:
                    d2.pop(s[l])
                l += 1
            if d1 == d2:
                ans.append(l)
        return ans

# Sliding Window + Frequency