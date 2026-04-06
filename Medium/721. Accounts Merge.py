from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        
        parent = {}
        email_to_name = {}
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                parent[email] = email
                email_to_name[email] = name
        
        for acc in accounts:
            first_email = acc[1]
            for email in acc[2:]:
                union(first_email, email)
        
        groups = defaultdict(list)
        for email in parent:
            root = find(email)
            groups[root].append(email)
        
        res = []
        for root in groups:
            emails = sorted(groups[root])
            name = email_to_name[root]
            res.append([name] + emails)
        
        return res

# Union-Find
# Connectivity
# Merging to first email works because even if the email doesn't exist; root of the email would be the first