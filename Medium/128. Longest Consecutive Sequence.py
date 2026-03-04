class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for i in s:
            if i - 1 not in s:
                count, j = 1, i
                while j + 1 in s:
                    count += 1
                    j += 1
                maxi = max(count, maxi)
        return maxi
    
# Sets Problem
# Iteration is fine as long as its only done once per sequence