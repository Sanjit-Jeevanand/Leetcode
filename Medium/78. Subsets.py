class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(i, curr):
            if i == len(nums):
                ans.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
        dfs(0, [])
        return ans
    
# State: I have x and curr; what should I do next?
# Choices: 
#   - Include x and recurse
#   - Exclude x and recurse
# Base Case: if i == n -> append curr and return