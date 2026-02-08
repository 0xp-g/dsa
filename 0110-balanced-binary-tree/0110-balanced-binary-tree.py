# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node) -> int:

            if node == None:
                return 0

            rdepth = dfs(node.right)
            ldepth = dfs(node.left)

            if abs(rdepth - ldepth) > 1:
                return -1

            if rdepth == -1 or ldepth == -1:
                return -1

            else:
                return 1 + max(rdepth, ldepth)
        
        return False if dfs(root) == -1 else True