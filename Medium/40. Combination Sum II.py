class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        nums = sorted(candidates)
        n = len(nums)
        def comb(curr, start, s):
            if s == target:
                ans.append(curr.copy())
                return
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                if s+nums[i] > target:
                    break
                curr.append(nums[i])
                comb(curr,i+1,s+nums[i])
                curr.pop()
        comb([],0,0)
        return ans