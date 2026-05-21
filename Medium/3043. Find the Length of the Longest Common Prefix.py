class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s1 = set()
        ans = 0
        for i in arr1:
            while i:
                s1.add(i)
                i //= 10
        for i in arr2:
            while i:
                if i in s1:
                    ans = max(ans,i)
                i //= 10
        return len(str(ans)) if ans else 0