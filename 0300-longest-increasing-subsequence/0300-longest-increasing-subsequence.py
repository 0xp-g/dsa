class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            cand = float('-inf')
            for j in range(i):
                if nums[j] < nums[i]:
                    cand = max(cand, 1 + dp[j])
            dp[i] = 1 if cand == float('-inf') else cand
        return max(dp)