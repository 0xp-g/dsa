# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr= []
        self.traverse(arr, root)
        return arr
    
    def traverse(self, arr, node):
        if not node:
            return 
        arr.append(node.val)
        self.traverse(arr, node.left)
        self.traverse(arr, node.right)
        return 