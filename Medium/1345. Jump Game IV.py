class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = defaultdict(list)
        n = len(arr)
        for i in range(n):
            d[arr[i]].append(i)
        q = deque([0])
        dp = [float('inf')]*n
        dp[0] = 0
        while q:
            i = q.popleft()
            if i > 0 and dp[i]+1 < dp[i-1]:
                q.append(i-1)
                dp[i-1] = dp[i]+1
            if i < n-1 and dp[i]+1 < dp[i+1]:
                q.append(i+1)
                dp[i+1] = dp[i]+1
            for j in d[arr[i]]:
                if dp[i]+1 < dp[j]:
                    q.append(j)
                    dp[j] = dp[i]+1
            d[arr[i]].clear()
        return dp[-1]
    

# Pure BFS Traversal or BFS + DP