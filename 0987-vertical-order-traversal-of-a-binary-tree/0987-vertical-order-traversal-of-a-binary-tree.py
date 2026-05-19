# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_map = defaultdict(list)
        ans = []
        def dfs(node, r, c):

            if not node:
                return
            col_map[c].append((node.val, r))
            dfs(node.left, r+1, c-1)
            dfs(node.right, r + 1, c+1)
            return
        dfs(root, 0, 0)
        hmap = dict(sorted(col_map.items(), key = lambda x:x[0]))
        print(hmap)
        res = []
        for ls in hmap.values():
            res.append(sorted(ls, key = lambda x:(x[1], x[0])))
        print(res)
        for i in range(len(res)):
            temp = []
            for j in range(len(res[i])):
                temp.append(res[i][j][0])
            ans.append(temp)
        return ans