class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d = defaultdict(int)
        n = len(A)
        ans = []
        count = 0
        for i in range(n):
            d[A[i]] += 1
            if d[A[i]] == 0:
                count += 1
            d[B[i]] -= 1
            if d[B[i]] == 0:
                count += 1
            ans.append(count)
        return ans