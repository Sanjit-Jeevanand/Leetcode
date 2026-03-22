class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def dfs(curr, i):
            ans.append(curr.copy())
            for j in range(i,n):
                curr.append(nums[j])
                dfs(curr, j+1)
                curr.pop()
        dfs([],0)
        return ans

# State: curr, i
# Choices: Among all next integers what to include
# Base Case: N/A