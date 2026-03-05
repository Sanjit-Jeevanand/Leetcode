class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        psum, length = 0,sum(nums)
        if length < target:
            return 0
        for i in range(len(nums)):
            psum += nums[i]
            while psum >= target:
                psum -= nums[left]
                length = min(length, i-left+1)
                left += 1
        return length

# Sliding window with Slow/Fast Pointer