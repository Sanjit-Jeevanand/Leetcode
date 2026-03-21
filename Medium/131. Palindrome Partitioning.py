class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        def isPal(st):
            l = 0
            r = len(st)-1
            while l <= r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True
        def part(curr, start):
            if start == n:
                ans.append(curr.copy())
                return
            for i in range(start,n):
                st = s[start: i+1]
                if isPal(st):
                    curr.append(st)
                    part(curr, i+1)
                    curr.pop()
        part([],0)
        return ans

# For-Loop Expansion
# State: curr, start
# Choices: try choices and recurse every possible palindrome in the rest
# Base Case: start == n

# Same as other Qs but instead of choosing next element; we choose next substring which is a Palindrome