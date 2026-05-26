class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set()
        s2 = set()
        count = 0
        for i in word:
            if (ord(i)+32 in s or ord(i)-32 in s) and ord(i) not in s2:
                count += 1
                s2.add(ord(i))
                s2.add(ord(i)+32)
                s2.add(ord(i)-32)
            s.add(ord(i))
        return count