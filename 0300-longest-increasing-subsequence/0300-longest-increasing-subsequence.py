class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        res = [nums[0]]
        for i in range(1, n):
            if nums[i] > res[-1]:
                res.append(nums[i])
                continue
            else:
                idx = bisect_left(res, nums[i])
                res[idx] = nums[i]
        return len(res)