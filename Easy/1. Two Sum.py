class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in seen:
                return[seen[comp],i]
            seen[nums[i]] = i


# Store complements in a dictionary; use look up to find if it exists in previous numbers