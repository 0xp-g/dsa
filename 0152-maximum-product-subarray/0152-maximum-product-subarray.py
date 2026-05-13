class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lmin = nums[0]
        lmax = nums[0]
        gmax = nums[0]
        for x in nums[1:]:
            temp = lmax
            lmax = max(lmax * x, x, lmin*x)
            lmin = min(temp*x, x, lmin*x)
            gmax = max(gmax, lmax)
        return gmax