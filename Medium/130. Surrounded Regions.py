class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(i,j):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != 'O':
                return
            board[i][j] = "#"
            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(i+di, j+dj)
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

# Introducing a third value to safekeep specific "O"s; 
# Here boundary "O"s which can never be surrounded