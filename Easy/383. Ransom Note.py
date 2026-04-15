class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        d = defaultdict(int)
        for i in m:
            d[i] += 1
        for i in r:
            d[i] -= 1
        return all(d[x] >= 0 for x in d)