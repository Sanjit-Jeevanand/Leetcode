class Solution:
    def maxArea(self, nums: List[int]) -> int:
        maxi = 0
        n = len(nums)
        left,right = 0, n-1
        while left < right:
            maxi = max(maxi, (right - left) * min(nums[left], nums[right]))
            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1
        return maxi
    
# Two Pointer with Area Calculation
# Shrink the shorter wall; update area if larger