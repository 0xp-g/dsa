# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node):
            if node.right == None and node.left == None:
                return 1
            left_height = 1 + dfs(node.left) if node.left else 0
            right_height = 1 + dfs(node.right) if node.right else 0
            return max(left_height, right_height)
        return dfs(root)