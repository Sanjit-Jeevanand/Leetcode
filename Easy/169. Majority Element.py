class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                c = nums[i]
                count += 1
            elif c == nums[i]:
                count += 1
            else:
                count -= 1
        return c

# Boyer-Moore voting Algorithm
# 2 variables; count and c; if they keep cancelling out one another; the majority would remain