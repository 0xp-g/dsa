# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval = min(p.val, q.val)
        qval = max(p.val, q.val)
        def dfs(node):
            if not node or pval <= node.val <= qval:
                return node
            leftreturn = dfs(node.left)
            rightreturn = dfs(node.right)
            return leftreturn if leftreturn else rightreturn
        return dfs(root)