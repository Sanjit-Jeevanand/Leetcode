class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(arr):
            n = len(arr)
            a, b = arr[0], max(arr[0], arr[1])
            for i in range(2, n):
                a, b = b, max(a + arr[i], b)
            return b
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        return max(rob_linear(nums[0:n-1]), rob_linear(nums[1:n]))
    
# Cyclic -> 2 Linear