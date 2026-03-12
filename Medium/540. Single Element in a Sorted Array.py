class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (l+r)//2
            print(l,m,r,nums[m])
            if nums[m] == nums[m^1]:
                l = m + 1
            else:
                r = m
        return nums[l]
    
# "^" -> is the XOR Operator; basically here it is used to change the index
# If x is even -> it changes to the next index
# If x is odd -> it changes to the previous index
# Basically it flips the last Binary Digit