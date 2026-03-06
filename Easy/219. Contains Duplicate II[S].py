class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                    return True
            s.add(nums[i])
            while i - l >= k:
                s.remove(nums[l])
                l+=1
        return False
    
# Sliding Window Implementation