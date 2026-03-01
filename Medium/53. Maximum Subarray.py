class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < 0:
                nums[i-1] = 0
            nums[i] = nums[i] + nums[i-1]
            if nums[i] > maxi:
                maxi = nums[i]
        return maxi
    
# Kadane intuition
# Prefix with reset