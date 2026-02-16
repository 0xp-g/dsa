# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        hmap = defaultdict(list)
        res = []
        dq = deque()
        dq.append(root)
        depth = 0
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                hmap[depth].append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            depth += 1
        for _, v in hmap.items():
            res.append(v[-1])
        return res