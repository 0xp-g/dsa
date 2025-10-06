class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        return self.solve(nums, k) - self.solve(nums, k-1)
    def solve(self, nums, k):
        left = 0
        csum = 0
        res = 0
        for right in range(len(nums)):
            csum += nums[right]
            while left <= right and csum > k:
                csum -= nums[left]
                left += 1
            res += right - left + 1
        return res