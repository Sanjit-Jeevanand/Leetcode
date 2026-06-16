# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 1
        def solve(node):
            nonlocal ans
            if not node: return 0
            u,v = 0,0
            if node.left:
                if node.val == node.left.val: 
                    u = solve(node.left)
                else:
                    solve(node.left)
            if node.right:
                if node.val == node.right.val:
                    v = solve(node.right)
                else:
                    solve(node.right)
            ans = max(ans, 1+u+v)
            return 1+max(u,v)
        solve(root)
        return ans-1