# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_same_or_not(p, q) -> bool:
            if not p and not q:
                return True
            if not p and q:
                return False
            if not q and p:
                return False
            if p.val != q.val:
                return False
            return is_same_or_not(p.right, q.left) and is_same_or_not(p.left, q.right)
        return is_same_or_not(root.left, root.right)