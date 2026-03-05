class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, length = 0, 0
        st = set()
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[l])
                l += 1
            st.add(s[i])
            length = max(length, i - l + 1)
        return length

# Set + Sliding Window
# Invariated: No duplicate in the window