# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def dfs(node):
            nonlocal arr
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        n = len(arr)
        for i in range(n-1):
            if arr[i+1] < arr[i]:
                firstconflict = arr[i]
                temp = i
                break
        for i in range(temp, n-1):
            if arr[i+1] < arr[i]:
                secondconflict = arr[i+1]
        print(firstconflict, secondconflict)
        def dfs(node, a, b):
            if not node:
                return
            if node.val == a:
                node.val = b
            elif node.val == b:
                node.val = a
            dfs(node.left, a, b)
            dfs(node.right, a, b)
            return
        dfs(root, firstconflict, secondconflict)
        return root