class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        ans = []
        def dfs(start,curr):
            ans.append(curr.copy())
            for i in range(start,n):
                if i > start and nums[i-1] == nums[i]:
                    continue
                curr.append(nums[i])
                dfs(i+1, curr)
                curr.pop()
        dfs(0,[])
        return ans
    
# Choice Expansion Tree
# State: Given start and curr what decision should I make
# Choice: Choose an element from start to n-1
# Base Case: No Explicit Base Case; loop ends; append curr to answer