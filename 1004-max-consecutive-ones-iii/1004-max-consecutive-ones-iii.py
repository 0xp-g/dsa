class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, res = 0, 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                k -= 1
            while l <= r and k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            res = max(res, r-l+1)
        return res