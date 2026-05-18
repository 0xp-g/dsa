# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node):
            nonlocal res
            if not node.left and not node.right:
                return 0
            
            right_depth = 1 + dfs(node.right) if node.right else 0
            left_depth = 1 + dfs(node.left) if node.left else 0
            res = max(res, right_depth+left_depth)
            return max(right_depth, left_depth)
        
        dfs(root)
        return res