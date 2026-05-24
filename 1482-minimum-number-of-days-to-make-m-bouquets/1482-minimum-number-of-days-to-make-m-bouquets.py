class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1
        
        def helper(mid):
            count = 0
            temp = 0
            for x in bloomDay:
                if x <= mid:
                    temp += 1
                else:
                    temp = 0

                if temp == k:
                    count += 1
                    temp = 0
            return count >= m
        
        l = 1
        r = 10 ** 9
        res = -1
        while l <= r:
            mid = (l+r) // 2
            if helper(mid):
                res = mid
                r = mid-1
            else:
                l = mid + 1
        return res