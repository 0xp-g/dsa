class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        res = inf
        for i in range(n):
            csum = 0
            for j in range(i, n):
                csum += nums[j]
                if l <= j - i + 1 <= r and csum > 0:
                    res= min(res, csum)
        return res if res != inf else -1