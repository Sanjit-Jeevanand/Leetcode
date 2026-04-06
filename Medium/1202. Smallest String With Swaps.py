class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x,y):
            x,y = find(x),find(y)
            if y!=x:
                parent[y] = x
        n = len(s)
        parent = [0]*n
        for i in range(n):
            parent[i] = i
        for i,j in pairs:
            union(i,j)
        groups = defaultdict(list)
        groups_c = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)
            groups_c[root].append(s[i])
        for i in groups_c:
            groups_c[i] = sorted(groups_c[i])[::-1]
        ans = ""
        for i in range(n):
            ans += groups_c[find(i)].pop()
        return ans
    
# Union-Find
# Connectivity
# 2 Dicts as group and mapping