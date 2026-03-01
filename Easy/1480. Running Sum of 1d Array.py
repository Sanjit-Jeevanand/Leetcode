class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums
    
# Running Sum or Prefix Sum pattern
# Compute Values till the certain index and add the index to get previous sum