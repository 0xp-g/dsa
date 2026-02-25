# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        dq = deque()
        dq.append((root, 1))
        minidx = 1
        maxidx = 1
        maxw = 0

        while dq:
            minidx = dq[0][1]
            maxidx = dq[-1][1]
            for _ in range(len(dq)):
                node, idx = dq.popleft()
                if node.left:
                    dq.append((node.left, idx << 1))
                if node.right:
                    dq.append((node.right, (idx << 1) + 1))
            maxw = max(maxw, maxidx - minidx + 1)

        return maxw