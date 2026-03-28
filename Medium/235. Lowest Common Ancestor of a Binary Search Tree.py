# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pr = min(p.val,q.val)
        qr = max(p.val, q.val)
        def dfs(node):
            if not node:
                return 
            if pr <= node.val <= qr:
                return node
            if node.val >= qr:
                return dfs(node.left)
            else:
                return dfs(node.right)
        return dfs(root)
    
# DFS on BST
# DFS with early termination pattern