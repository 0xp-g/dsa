# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        i = 0
        maxw = i
        if not root:
            return 0
        dq = deque([(root, 0)])
        while dq:
            tempmin, tempmax = dq[0][1], dq[-1][1] 
            maxw = max(maxw, abs(tempmin - tempmax))
            for _ in range(len(dq)):
                node, i = dq.popleft()
                if node.left:
                    dq.append((node.left, 2*i+1))
                if node.right:
                    dq.append((node.right, 2 * i + 2))
        return maxw + 1