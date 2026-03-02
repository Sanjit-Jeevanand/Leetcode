class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp, rp = 1,1
        ans = []
        for i in range(n):
            ans.append(lp)
            lp *= nums[i]
        for i in range(n):
            ans[n-i-1] *= rp
            rp *= nums[n-i-1]
        return ans

# Maintain two invariants left product and right product
# multiply by one off