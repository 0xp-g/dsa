class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_possible = 0
        for i in range(n):
            if i > max_possible:
                return False
            max_possible = max(max_possible, i+nums[i])
            if max_possible >= n-1:
                return True
        return False