class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif  nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: 
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# Binary Search -> Rotated Array
# On dividing 2 halfs emerge:
# Sorted Half
# Rotated Array
# If target exists in Sorted half; perform normal binary search on that
# Else Check the rotated array again