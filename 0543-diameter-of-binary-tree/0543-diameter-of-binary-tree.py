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
            if node == None:
                return 0
                
            rightlen = 1 + dfs(node.right)  
            leftlen = 1 + dfs(node.left)    
            
            res = max(res, rightlen + leftlen - 1)
            
            return max(rightlen, leftlen)
        
        dfs(root)
        return max(0, res - 1)