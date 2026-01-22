class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        S = sum(nums)
        if S % 2 == 1:
            return False
        @lru_cache(None)
        def dp(i, target):
            if target < 0 or i <= -1:
                return False
            if target == 0:
                return True
            if dp(i-1, target-nums[i]) or dp(i-1, target):
                return True
            return False
        return dp(n-1, S/2)