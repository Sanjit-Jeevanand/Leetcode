class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        left = [0] * len(nums)
        n = len(nums)
        def per(curr, left):
            if len(curr) == n:
                ans.append(curr.copy())
                return
            for i in range(n):
                if left[i] == 0:
                    curr.append(nums[i])
                    left[i] = 1
                    per(curr, left)
                    left[i] = 0
                    curr.pop()
        per([], left)
        return ans
    
# Permutation Backtracking Pattern
# Pick any unused element at each step