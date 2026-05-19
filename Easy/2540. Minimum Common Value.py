class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if nums1[-1] < nums2[0] or nums2[-1] < nums1[0]: return -1
        l = 0
        n = len(nums2)
        for i in nums1:
            while i > nums2[l] and l < n-1:
                l += 1
            if i == nums2[l]:
                return i
        return -1