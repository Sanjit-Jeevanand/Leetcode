class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s = []
        n = len(nums)
        ans = [-1] * n
        for i in range(2*n):
            while s and nums[i%n] > nums[s[-1]]:
                v = s.pop()
                ans[v] = nums[i%n]
            if i < n:
                s.append(i)
        return ans

# Modulo to make array circular
# Stack only saving i till n