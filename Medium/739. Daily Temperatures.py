class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        n = len(temp)
        ans = [0]*n
        for i in range(n):
            while stack and temp[i] > temp[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
    
# Monotonic Stack
# Each day waits for a warmer day