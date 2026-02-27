# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = dict()
        for i, v in enumerate(inorder):
            hmap[v] = i
        #whys this so hard brh
        def solve(prestart, preend, instart, inend):
            if prestart > preend or instart > inend:
                return None
            root_val = preorder[prestart]
            root_idx = hmap[root_val]
            node = TreeNode(root_val)
            left_size = root_idx - instart
            node.left = solve(prestart + 1, prestart + 1 + left_size, instart, root_idx - 1)
            node.right = solve(prestart + left_size + 1, preend, root_idx + 1, inend)
            return node
        return solve(0, len(preorder)-1, 0, len(inorder)-1)