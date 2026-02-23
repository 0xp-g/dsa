class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        prefmax = [-1] * n
        suffmax = [-1] * n
        prefmax[0] = height[0]
        suffmax[n-1] = height[n-1]
        res = 0

        for i in range(1, n):
            prefmax[i] = max(prefmax[i-1], height[i])

        for i in range(n-2, -1, -1):
            suffmax[i] = max(suffmax[i+1], height[i])

        for i in range(n):
            res += min(prefmax[i], suffmax[i]) - height[i]
            
        return res