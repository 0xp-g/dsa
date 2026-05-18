# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            if left_sum < 0: left_sum = 0
            if right_sum < 0: right_sum = 0
            current_path_sum = node.val + left_sum + right_sum
            res = max(res, current_path_sum)
            return max(node.val + left_sum, node.val + right_sum)
        dfs(root)
        return res