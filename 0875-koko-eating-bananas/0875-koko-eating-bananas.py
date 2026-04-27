class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def solve(k):
            hours = 0
            for pile in piles:
                if pile <= k:
                    hours += 1
                    continue
                else:
                    hours += ceil(pile/k)
            return hours <= h
        
        l, r = 1, 10 ** 9
        res = None

        while l <= r:
            mid = (l+r) // 2
            if solve(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res