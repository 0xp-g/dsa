# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        par_map = dict()
        res = list()
        dq = deque()
        par_map[root] = []
        def dfs(node, par):
            if not node:
                return 
            if par != -1:
                par_map[node] = par
            if node == target:
                dq.append(node)
            dfs(node.left, node)
            dfs(node.right, node)
            return
        dfs(root, -1)
        level = 0
        vis = set()
        while dq:
            if level == k:
                while dq:
                    res.append(dq.popleft().val)
            for _ in range(len(dq)):
                node = dq.popleft()
                if node != root and par_map[node] not in vis:
                    dq.append(par_map[node])
                 #obviously theres only a single parent
                #this is to prevent writing a separate case for the root
                vis.add(node)
                if node.left and node.left not in vis:
                    dq.append(node.left)
                if node.right and node.right not in vis:
                    dq.append(node.right)
            level += 1
        return res