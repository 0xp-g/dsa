class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        if n % 2 == 1:
            ref = nums[n//2]
            for num in nums:
                res += abs(ref - num)
            return res
        else:
            ref = (nums[n//2] + nums[(n//2)-1]) // 2
            for num in nums:
                res += abs(ref - num)
            return res
        return