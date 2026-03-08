class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        n = len(nums)
        l = 0
        ans = 0
        for i in range(n):
            prod *= nums[i]
            while prod >= k:
                prod //= nums[l]
                l += 1
            ans += i - l + 1
        return ans
    
# Sliding Window
# Every Subarray inside [l....i] is valid; hence count can be increased like that