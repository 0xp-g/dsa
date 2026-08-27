class Solution:
    def longestSubarray(self, nums: list[int], k: int) -> int:
        res = 0
        n = len(nums)

        def factors(n):
            res = set()
            i = 2
            while i * i <= n:
                while n % i == 0:
                    res.add(i)
                    n //= i
                i += 1
            if n > 1:
                res.add(n)
            return res
        
        memo = {}

        l = 0
        cmap = dict()

        for r in range(n):
            if nums[r] in memo:
                res_fac = memo[nums[r]]
            else:
                res_fac = factors(nums[r])
                memo[nums[r]] = res_fac
            
            for u in res_fac:
                if u not in cmap:
                    cmap[u] = 1
                else:
                    cmap[u] += 1
            
            while l <= r and len(cmap) > k:

                for v in memo[nums[l]]:
                    cmap[v] -= 1
                    if cmap[v] == 0:
                        del cmap[v]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res