# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque()
        dq.append(root)
        res = []
        while dq:
            n = len(dq)
            tot = 0
            for _ in range(n):
                node = dq.popleft()
                tot += node.val
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
            res.append(tot/n)
        return res