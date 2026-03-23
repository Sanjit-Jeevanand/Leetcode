class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def nq(pos, diag1, diag2, start):
            if len(pos) == n:
                curr = []
                for i in pos:
                    temp = ["."]*n
                    temp[i] = "Q"
                    curr.append("".join(temp))
                ans.append(curr.copy())
                return
            for i in range(n):
                if i not in pos and start + i not in diag1 and start - i not in diag2:
                    pos.append(i)
                    diag1.add(start+i)
                    diag2.add(start-i)
                    nq(pos, diag1, diag2, start+1)
                    pos.pop()
                    diag1.remove(start + i)
                    diag2.remove(start - i)
        nq([],set(),set(),0)
        return ans
    
# Constraint: not in j, i+j or i-j