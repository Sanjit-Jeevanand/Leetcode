class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        q = deque([start])
        visited.add(start)
        while q:
            i = q.popleft()
            if 0 <= i + arr[i] < n and i + arr[i] not in visited:
                q.append(arr[i]+i)
                visited.add(i+arr[i])
            if 0 <= i - arr[i] < n and i - arr[i] not in visited:
                q.append(i-arr[i])
                visited.add(i-arr[i])
            if arr[i] == 0:
                return True
        return False
    
# Graph BFS