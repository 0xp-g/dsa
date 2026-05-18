# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = deque([root])
        level = -1
        res = []
        while dq:
            depth = []
            level += 1
            for _ in range(len(dq)):
                node = dq.popleft()
                depth.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if level % 2 == 0:
                res.append(depth) 
            else:
                res.append(depth[::-1])
        return res