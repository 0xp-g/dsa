class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        prefmax = [-1] * length
        suffmax = [-1] * length
        prefmax[0] = height[0]
        suffmax[length-1] = height[length-1]
        water = 0
        for ptr in range(1, length):
            prefmax[ptr] = max(height[ptr], prefmax[ptr-1])
        for ptr in range(length-2, -1, -1):
            suffmax[ptr] = max(height[ptr], suffmax[ptr+1])
        for bar in range(length):
            water += min(prefmax[bar], suffmax[bar]) - height[bar]
        return water