# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node):
            nonlocal ans
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left < 0:
                left = 0
            if right < 0:
                right = 0
            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return ans
    
# While calculating answer, use sum of l and r
# but while passing the answer upwards only one node can be expanded