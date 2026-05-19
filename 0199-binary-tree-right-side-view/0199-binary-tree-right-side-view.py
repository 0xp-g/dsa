# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        row_map = defaultdict(list)
        def dfs(node, r, c):
            if not node:
                return
            dfs(node.right, r+1, c+1)
            row_map[r].append((node.val))
            dfs(node.left, r+1, c-1)
        dfs(root, 0, 0)
        row_map = dict(sorted(row_map.items()))
        for v in row_map.values():
            res.append(v[0])
        return res