class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if ("row", i, val) in seen or \
                ("col", j, val) in seen or \
                ("box", i//3, j//3, val) in seen:
                    return False
                seen.add(("row", i, val))
                seen.add(("col", j, val))
                seen.add(("box", i//3, j//3, val))
        return True