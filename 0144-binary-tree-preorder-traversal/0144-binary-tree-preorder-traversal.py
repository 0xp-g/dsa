# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        st = []
        st.append(root)
        while st:
            node = st.pop()
            if node == None:
                continue
            res.append(node.val)
            st.append(node.right)
            st.append(node.left)
        return res