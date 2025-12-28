class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        pre = [0] * n
        suff = [0] * n
        dp = [0] * n

        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = max(nums[i], pre[i - 1])

        suff[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = min(nums[i], suff[i + 1])

        dp[n - 1] = pre[n - 1]
        for i in range(n - 2, -1, -1):
            dp[i] = pre[i]
            if pre[i] > suff[i + 1]:
                dp[i] = dp[i + 1]

        return dp