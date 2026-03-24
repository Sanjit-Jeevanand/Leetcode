# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(curr, node, s):
            if node is None:
                return
            curr.append(node.val)
            s = s+node.val
            if node.left is None and node.right is None:
                if s == targetSum:
                    ans.append(curr.copy())
                curr.pop()
                return
            dfs(curr, node.left, s)
            dfs(curr, node.right, s)
            curr.pop()
        dfs([],root,0)
        return ans
    
# Don't forget to return curr to normal at leafnodes [curr.pop()]