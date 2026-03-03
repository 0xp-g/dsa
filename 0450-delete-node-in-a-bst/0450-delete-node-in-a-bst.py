# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def find_inorder_successor(node):
            current = node.right
            while current.left:
                current = current.left
            return current
        def delete(node, key):
            if not node:
                return None
            if key < node.val:
                node.left = delete(node.left, key)
            elif key > node.val:
                node.right = delete(node.right, key)
            else:
                if not node.right and not node.left:
                    return None
                if (node.right and not node.left) or (node.left and not node.right):
                    return node.right if node.right else node.left
                else:
                    successor = find_inorder_successor(node)
                    node.val = successor.val
                    node.right = delete(node.right, successor.val)
            return node
        return delete(root, key)