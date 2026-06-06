class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def best(i):
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(best(i-2) + nums[i], best(i-1))
        return best(n-1)