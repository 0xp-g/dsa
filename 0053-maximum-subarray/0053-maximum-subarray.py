class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        rsum = 0
        for i in range(len(nums)):
            rsum += nums[i]
            maxsum = max(maxsum, rsum)
            if rsum < 0:
                rsum = 0
        return maxsum