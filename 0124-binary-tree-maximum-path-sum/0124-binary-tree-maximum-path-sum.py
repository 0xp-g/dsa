# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -1001
        def dfs(node) -> int:
            nonlocal res
            if not node:
                return 0
            rsum = max(0, dfs(node.right))
            lsum = max(0, dfs(node.left))
            res = max(res, rsum + lsum + node.val)
            return node.val + max(rsum, lsum)
        dfs(root)
        return res
            