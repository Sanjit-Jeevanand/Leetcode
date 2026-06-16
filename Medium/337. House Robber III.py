# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def solve(node):
            if not node: return 0
            if node in memo: return memo[node]
            u,v = 0,0
            if node.left:
                u = solve(node.left.left) + solve(node.left.right)
            if node.right:
                v = solve(node.right.left) + solve(node.right.right)
            memo[node] = max(node.val + u + v, solve(node.left) + solve(node.right))
            return memo[node]
        return solve(root)