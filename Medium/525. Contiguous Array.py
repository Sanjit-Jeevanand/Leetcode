class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        psum = 0
        d = {0 : -1}
        length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                psum -= 1
            else:
                psum += 1
            if psum in d:
                length = max(length, i - d[psum])
            else:
                d[psum] = i
        return length
    
# Maintain prefix sum counter, calculate length if it exists in the dictionary