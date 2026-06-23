class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, sr: int, sc: int) -> int:
        MOD = 10**9 + 7
        memo = {}
        def solve(i, j, moves):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if moves == maxMove:
                return 0
            if (i, j, moves) in memo:
                return memo[(i, j, moves)]
            ans = 0
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ans += solve(i + di, j + dj, moves + 1)
            memo[(i, j, moves)] = ans % MOD
            return memo[(i, j, moves)]
        return solve(sr, sc, 0)