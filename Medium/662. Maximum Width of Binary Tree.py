# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        q = deque([(root,0)])
        while q:
            lvl_size = len(q)
            _, first = q[0]
            _, last = q[-1]
            ans = max(ans, last - first + 1)
            for _ in range(lvl_size):
                node, i = q.popleft()
                i -= first
                if node.left:
                    q.append((node.left, 2*i))
                if node.right:
                    q.append((node.right, 2*i+1))
        return ans
    
# Save index along with node; width = last - first + 1