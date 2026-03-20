class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        n = len(nums)
        left = [False]*n
        def per(curr, left):
            if len(curr) == n:
                ans.append(curr.copy())
                return
            for i in range(n):
                if left[i] == 0:
                    if i > 0 and nums[i] == nums[i-1] and not left[i-1]:
                        continue
                    curr.append(nums[i])
                    left[i] = True
                    per(curr, left)
                    curr.pop()
                    left[i] = False
        per([], left)
        return ans
    
# For Loop Recursion
# To skip duplicates; sort and maintain a check for previous elements