class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2 : ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']}
        ans = []
        n = len(digits)
        def let(curr, i):
            if i == n:
                ans.append(curr)
                return
            for l in d[int(digits[i])]:
                let(curr+l,i+1)
        let("",0)
        return ans
    
# State: curr, i
# Choices: Among letters associated with i, which should i pick
# Base Case: i == n
# Strings are immutable so you don't need to append and pop (backtrack)