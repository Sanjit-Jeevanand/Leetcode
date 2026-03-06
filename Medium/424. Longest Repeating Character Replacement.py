class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l, maxi, length = 0,0,0
        for i in range(len(s)):
            d[s[i]] += 1
            maxi = max(maxi, max(d.values()))
            while i - l + 1 - maxi > k:
                d[s[l]] -= 1
                l += 1
        length = max(length, i - l + 1)
        return length