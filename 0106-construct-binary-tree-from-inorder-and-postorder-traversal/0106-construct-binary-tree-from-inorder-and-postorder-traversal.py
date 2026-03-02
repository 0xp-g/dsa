# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hmap = defaultdict(int)
        n = len(postorder)
        for i, v in enumerate(inorder):
            hmap[v] = i
        def recurse(pstart, pend, instart, inend):
            if pstart>pend or instart>inend:
                return None
            root_pos = hmap[postorder[pend]]
            node = TreeNode(postorder[pend])
            right_size = inend - root_pos + 1
            left_size = root_pos - instart + 1
            node.left = recurse(pstart, pend - right_size, instart, root_pos - 1)
            node.right = recurse(pend - right_size + 1, pend - 1, root_pos + 1, inend)
            return node
        return recurse(0, n-1, 0, n-1)