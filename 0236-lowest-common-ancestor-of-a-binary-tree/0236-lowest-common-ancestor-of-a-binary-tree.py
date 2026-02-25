# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if node in [p, q, None]:
                return node
            
            left_res = dfs(node.left)
            right_res = dfs(node.right)

            return node if left_res and right_res else left_res or right_res
        
        return dfs(root)