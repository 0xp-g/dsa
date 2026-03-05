# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []
        def traverse(node, csum, ls):
            nonlocal res
            if csum == targetSum and not node.left and not node.right:
                res.append(ls[:])
            if node.left:
                ls.append(node.left.val)
                traverse(node.left, csum + node.left.val, ls)
                ls.pop()   
            if node.right:
                ls.append(node.right.val)
                traverse(node.right, csum + node.right.val, ls)
                ls.pop()    
            return res
        return traverse(root, root.val, [root.val])