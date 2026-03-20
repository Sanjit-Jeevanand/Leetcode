class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        cand = sorted(cand)
        ans = []
        n = len(cand)
        def comb(curr, start, s):
            if s == target:
                ans.append(curr.copy())
                return
            if s > target:
                return
            for i in range(start, n):
                if s + cand[i] > target:
                    break
                curr.append(cand[i])
                comb(curr, i, s + cand[i])
                curr.pop()
        comb([],0,0)
        return ans
    
# For Loop Exploration
# State: curr, start, s(sum)
# Choices: which element to pick
# Base Case s >= target