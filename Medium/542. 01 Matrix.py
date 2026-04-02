class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        ans = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    ans[i][j] = 0
        while q:
            i,j = q.popleft()
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n:
                    if ans[ni][nj] > ans[i][j] + 1:
                        ans[ni][nj] = ans[i][j] + 1
                        q.append((ni, nj))
        return ans
    
# Tracking Vistied using ans matrix
# BFS since it asks for shortest distance