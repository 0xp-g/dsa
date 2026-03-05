# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def findpred(node):
            while node.right:
                node = node.right
            return node
        def flatten(node):
            if not node:
                return
            if node.left:
                predecessor = findpred(node.left)
                predecessor.right = node.right
                node.right = node.left
                node.left = None
            flatten(node.right)
            return node
        return flatten(root)