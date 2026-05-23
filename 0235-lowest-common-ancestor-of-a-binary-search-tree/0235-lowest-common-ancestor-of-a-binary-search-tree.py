# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval, qval = min(p.val, q.val), max(p.val, q.val)
        
        def dfs(node):

            if not node:
                return
            
            if pval == node.val or qval == node.val:
                return node
            
            if pval < node.val and qval > node.val:
                return node
            
            if node.val < p.val and node.val < q.val:
                return dfs(node.right)
            
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left)

        return dfs(root)