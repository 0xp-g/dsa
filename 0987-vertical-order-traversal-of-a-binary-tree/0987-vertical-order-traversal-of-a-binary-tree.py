# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        hmap = dict()
        def bfs(node, row, col):
            nonlocal hmap
            if not node:
                return
            if col not in hmap:
                hmap[col] = []
            hmap[col].append((node.val, row))
            bfs(node.left, row + 1, col-1)
            bfs(node.right, row + 1, col+1)
        bfs(root, 0, 0)
        hmap = dict(sorted(hmap.items(), key = lambda x : x[0]))
        for k, v in hmap.items():
            ls = sorted(v, key=lambda x:(x[1], x[0]))
            res.append([x[0] for x in ls])
        return res