class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(n):
            temp = sum(ceil(x/n) for x in nums)
            if temp <= threshold:
                return True
            return False
        l = 1
        r = max(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res