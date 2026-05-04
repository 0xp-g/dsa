class Solution:
    def trap(self, height: List[int]) -> int:
        n, water = len(height), 0
        prefmax = [0] * n
        suffmax = [0] * n
        prefmax[0] = height[0]
        suffmax[n-1] = height[n-1]
        for i in range(1, n):
            prefmax[i] = max(height[i], prefmax[i-1])
        for i in range(n-2, -1, -1):
            suffmax[i] = max(height[i], suffmax[i+1])
        for i in range(n):
            water += min(prefmax[i], suffmax[i]) - height[i]
        return water