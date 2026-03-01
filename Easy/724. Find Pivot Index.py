class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = 0
        lsum = 0
        n = len(nums)
        for i in range(n):
            total_sum += nums[i]
        for i in range(n):
            if total_sum - nums[i] == 2*lsum:
                return i
            lsum += nums[i]
        return -1

# Calculate Total Sum
# Compare with prefix sum