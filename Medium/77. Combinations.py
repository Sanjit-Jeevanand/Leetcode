class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def comb(start, curr):
            x = len(curr)
            if x == k:
                ans.append(curr.copy())
                return
            for i in range(start, n - (k - x) + 2):
                curr.append(i)
                comb(i+1, curr)
                curr.pop()
        comb(1,[])
        return ans
    
# State: curr, i
# Choices: Which element to pick next
# Base Case: len(curr) == k

# For loop expansion pattern