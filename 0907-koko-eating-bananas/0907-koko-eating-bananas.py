class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(n):

            res = sum(ceil(x / n) for x in piles)

            return True if res <= h else False

        l = 1
        res = r = max(piles)

        while l <= r:

            mid = (l + r)//2

            if check(mid):
                res = mid
                r = mid - 1
                
            else:
                l = mid + 1

        return res