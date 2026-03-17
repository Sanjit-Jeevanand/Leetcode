class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        ans=[]
        for i in range(len(nums)):
            while dq and i - k + 1 > dq[0]:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans[k-1:]
    
# Deque
# First loop removes any element which is not part of the window
# Second loop removes any older and weaker element