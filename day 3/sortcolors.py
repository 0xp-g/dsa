# NOT FULLY OPTIMIZED.
class Solution:
    def sortZeroOneTwo(self, nums):
        x= y= z=ind = 0
        for num in nums:
            if num == 0:
                x += 1
            elif num == 1:
                y += 1
            else:
                z += 1
        for c, v in [(x,0),  (y, 1), (z, 2)]:
            for _ in range(c):
                nums[ind] = v
                ind += 1
        return nums
    
