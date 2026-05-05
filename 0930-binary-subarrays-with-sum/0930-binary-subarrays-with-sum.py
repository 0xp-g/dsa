class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        def atmost(k):
            l, r = 0, n-1
            res, rsum = 0, 0
            for r in range(n):
                rsum += nums[r]
                while l <= r and rsum > k:
                    rsum -= nums[l]
                    l += 1
                res += r-l+1
            return res
        return atmost(goal) - atmost(goal-1)