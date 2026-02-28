class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        ans = set()
        for num in nums1:
            s.add(num)
        for num in nums2:
            if num in s:
                ans.add(num)
        return list(ans)

# Set for memory structure; recheck once written