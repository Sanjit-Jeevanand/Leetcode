class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nz = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[nz] = nums[nz],nums[i]
                nz += 1
        return nums
    
# Two Pointers Pattern
# Skeleton :

# write = 0

# for i from 0 to n-1:

#     if nums[i] != 0:
#         swap nums[i] with nums[write]
#         write += 1