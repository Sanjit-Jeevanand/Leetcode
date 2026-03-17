class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        d = {}
        ans = []
        for x in nums2:
            while stack and x > stack[-1]:
                idx = stack.pop()
                d[idx] = x
            stack.append(x)
        for x in nums1:
            ans.append(d.get(x, -1))
        return ans