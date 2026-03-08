class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d = defaultdict(int)
        ans = 0
        count = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(len(s)):
            if s[i] in vowels:
                count += 1
            if i >= k and s[i-k] in vowels:
                count -= 1
            ans = max(ans,count)
        return ans


# Sliding window with a counter