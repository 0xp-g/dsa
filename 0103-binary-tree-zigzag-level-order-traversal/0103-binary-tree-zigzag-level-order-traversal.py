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
        dq = deque()
        dq.append(root)
        res = []
        cnt = 0
        while dq:
            temp = []
            cnt += 1
            #run loop till dq's length to simulate level wise
            for _ in range(len(dq)):
                node = dq.popleft()
                temp.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if cnt % 2 == 0:
                res.append(temp[::-1])
            else:
                res.append(temp)
        return res

