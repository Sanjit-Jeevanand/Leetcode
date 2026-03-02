class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        psum = sum(nums[:k])
        maxi = psum
        for i in range(k, len(nums)):
            psum = psum + nums[i] - nums[i-k]
            maxi = max(psum, maxi)
        return maxi/k

# prefix sum but with condition
# form the window first