class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        l1,r1 = 0, n-1
        while l1 <= r1:
            mid = (l1+r1) // 2
            if nums[mid] >= target:
                r1 = mid - 1
            else:
                l1 = mid + 1
            print(l1,r)
        if l1 < n and nums[l1] == target: 
            return [l1, r]
        return[-1,-1]
    
# Two Binary Searches to find the boundaries