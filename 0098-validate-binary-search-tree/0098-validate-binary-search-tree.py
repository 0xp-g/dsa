# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''        def validate(node):
                    if not node: #node-none
                        return True
                    if node.right and node.left: #2 children case
                        if node.left.val < node.val < node.right.val:
                            if not validate(node.right):
                                return False
                            if not validate(node.left):
                                return False
                        else:
                            return False
                    elif not node.right and not node.left: #no children case
                        return True
                    else: #1 children case
                        if node.left:#left child
                            if node.left.val < node.val:
                                if not validate(node.left):
                                    return False
                            else:
                                return False
                        else:#right child
                            if node.right.val > node.val:
                                    if not validate(node.right):
                                        return False
                            else:
                                return False
                    return True'''
        def validate(node, localmax, localmin):
            if not node:
                return True
            if node.val >= localmax or node.val <= localmin:
                return False
            return validate(node.left, node.val, localmin) and validate(node.right,localmax,node.val)
        return validate(root, float('inf'), float('-inf'))