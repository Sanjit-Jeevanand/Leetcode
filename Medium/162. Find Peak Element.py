class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l , r = 0 , len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l
    
# Binary Search -> Boundary Condition
# Remember l < r not l <= r
# if nums[mid] < nums[mid+1] -> Peak must exist in the right; else it exists in the left half